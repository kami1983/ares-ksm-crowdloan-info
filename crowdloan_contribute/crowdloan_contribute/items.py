# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

# 贡献人信息
class ContributorItem(Item):
    address = Field()  # 'address': 'GezcmEVJAKbF691jGtwknuVmGZAkcMVZ6W9uhiuHJPDkxyz',
    display = Field()  # 'display': '',
    judgements = Field()  # 'judgements': None,
    account_index = Field()  # 'account_index': '',
    identity = Field()  # 'identity': False,
    parent = Field()  # 'parent': None,
    pass

# 区块信息
class ExtrinsicItem(Item):
    fund_id = Field()  # 'fund_id': '2008-10',
    para_id = Field()  # 'para_id': 2008,
    who = Field()  # 'who': 'GezcmEVJAKbF691jGtwknuVmGZAkcMVZ6W9uhiuHJPDkxyz',
    contributed = Field()  # 'contributed': '210999000000',
    contributing = Field()  # 'contributing': '210999000000',
    block_num = Field()  # 'block_num': 8026933,
    block_timestamp = Field()  # 'block_timestamp': 1624373106,
    extrinsic_index = Field()  # 'extrinsic_index': '8026933-5',
    status = Field()  # 'status': 1,
    memo = Field()  # 'memo': ''
    pass




