# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from crowdloan_contribute.items import ContributorItem, ExtrinsicItem

class CrowdloanContributePipeline:
    def process_item(self, item, spider):
        if isinstance(item,  ContributorItem):

            return item
        elif isinstance(item, ExtrinsicItem):

            return item

        # print(item)
        # print("-----------")
        # return item
