import json
import scrapy
from crowdloan_contribute.items import ContributorItem, ExtrinsicItem


class SubscanSpider(scrapy.Spider):
    name = 'subscan'
    allowed_domains = ['kusama.subscan.io']
    start_urls = ['https://kusama.subscan.io/api/scan/parachain/contributes']

    page_size = 25 # 页面大小
    page_num = 0 # 页号
    fund_id = "2008-10" # 众贷ID

    # 定义请求头
    headers = {
        'authority': 'kusama.subscan.io',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://kusama.subscan.io',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://kusama.subscan.io/crowdloan_contribute/?fund_id=2008-10',
        'cookie': 'local_language=zh-CN; __gads=ID=1109176928f7ba91-223e36436eca0060:T=1626829353:RT=1626829353:S=ALNI_MbemXES5sfYvitdGGQ6rf4o6WcPtA; banner=true; _gid=GA1.2.231796429.1627253636; _ga_4Q4YQW2GZ3=GS1.1.1627253637.5.1.1627254119.0; _ga=GA1.1.549609681.1626829349; _gat_UA1525613143=1; _gat_UA1525613147=1'
    }

    # 生成一个请求
    def makeRequest(self) :
        # 页码
        data_raw = {"row": self.page_size, "page": self.page_num, "fund_id": self.fund_id}
        print("Make Request ------------")
        print(data_raw)
        # 循环要请求的地址信息
        return scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers, method='POST',
                             body=json.dumps(data_raw))

    def start_requests(self):
        yield self.makeRequest()

    def parse(self, response):
        result_data = json.loads(response.body)
        print("Get contributes count is :", len(result_data['data']['contributes']))
        for data in result_data['data']['contributes'] :
            # 解析到 Item 中
            extrinsic_item = ExtrinsicItem()
            extrinsic_item['fund_id'] = data['fund_id']
            extrinsic_item['para_id'] = data['para_id']
            extrinsic_item['who'] = data['who']
            extrinsic_item['contributed'] = data['contributed']
            extrinsic_item['contributing'] = data['contributing']
            extrinsic_item['block_num'] = data['block_num']
            extrinsic_item['block_timestamp'] = data['block_timestamp']
            extrinsic_item['extrinsic_index'] = data['extrinsic_index']
            extrinsic_item['status'] = data['status']
            extrinsic_item['memo'] = data['memo']

            yield extrinsic_item

            contributor_item = ContributorItem()
            contributor_item['address'] = data['who_display']['address']
            contributor_item['display'] = data['who_display']['display']
            contributor_item['judgements'] = data['who_display']['judgements']
            contributor_item['account_index'] = data['who_display']['account_index']
            contributor_item['identity'] = data['who_display']['identity']
            contributor_item['parent'] = data['who_display']['parent']

            yield contributor_item

        # 判断是否还有下一页的数据
        if len( result_data['data']['contributes']) >= self.page_size :
            # 理论上不大可能 > 25 因为我上面设定的页码数量就是 25
            # 如果进入这里证明还有下一页
            self.page_num += 1
            yield self.makeRequest()