# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import pytz
import datetime
from scrapy.item import Item, Field

# 贡献人信息
class ContributorItem(Item):

    address = Field()  # 'address': 'GezcmEVJAKbF691jGtwknuVmGZAkcMVZ6W9uhiuHJPDkxyz',
    display = Field()  # 'display': '',
    judgements = Field()  # 'judgements': None,
    account_index = Field()  # 'account_index': '',
    identity = Field()  # 'identity': False,
    parent = Field()  # 'parent': None,
    random_key = Field() # 关联的随机KEY

    @classmethod
    def TableNameOfMysql(cls):
        return "contributor_item"

    @classmethod  # 获取Mysql 的配置信息
    def TableSchemeOfMysql(cls):
        return ''' 
            CREATE TABLE IF NOT EXISTS `{}` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `address` varchar(50) NOT NULL,
      `display` varchar(45) DEFAULT NULL,
      `judgements` varchar(45) DEFAULT NULL,
      `account_index` varchar(45) DEFAULT NULL,
      `identity` varchar(45) DEFAULT NULL,
      `parent` varchar(45) DEFAULT NULL,
      `at_create` datetime DEFAULT NULL,
      `at_update` datetime DEFAULT NULL,
      `random_key` varchar(45) DEFAULT NULL,
      `other_status` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `item_unique` (`address`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
             '''.format(cls.TableNameOfMysql())

    # 这里的字段和顺序如果更新，那么 getInsertSqlValues 方法的顺序也必须更新
    # TODO::之后调整更新需要同步更新其他方法的问题
    def getInsertSqlTemplate ( self , table_name ):
        return '''
        INSERT INTO {}
(`address`, `display`, `judgements`, `account_index`, `identity`, `parent`, `at_create`, `at_update`, `random_key`) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
ON DUPLICATE KEY UPDATE 
`display`=%s, 
`judgements`= %s, 
`account_index`= %s, 
`identity`= %s, 
`parent`= %s, 
`at_update`= %s,
`random_key`= %s ;
        '''.format(table_name)

    def getInsertSqlValues(self, time_zone) :
        return [
            self['address'],
            self['display'],
            self['judgements'],
            self['account_index'],
            self['identity'],
            self['parent'],
            self.getCurrentTime(time_zone),
            self.getCurrentTime(time_zone),
            self['random_key'],
            #----- update
            self['display'],
            self['judgements'],
            self['account_index'],
            self['identity'],
            self['parent'],
            self.getCurrentTime(time_zone),
            self['random_key'],
        ]

    # 获取当前系统时间
    def getCurrentTime(self, time_zone):
        '''
        获取当前系统时间
        '''
        return datetime.datetime.now(pytz.timezone(time_zone)).strftime('%Y-%m-%d %H:%M:%S')

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
    random_key = Field()  # 关联的随机KEY

    @classmethod
    def TableNameOfMysql (cls):
        return "extrinsic_item"

    @classmethod  # 获取Mysql 的配置信息
    def TableSchemeOfMysql (cls) :
        return ''' 
        CREATE TABLE IF NOT EXISTS `extrinsic_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(20) NOT NULL,
  `para_id` varchar(20) NOT NULL,
  `who` varchar(50) NOT NULL,
  `contributed` varchar(45) NOT NULL,
  `contributing` varchar(45) NOT NULL,
  `block_num` varchar(45) NOT NULL,
  `block_timestamp` varchar(45) NOT NULL,
  `extrinsic_index` varchar(45) NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  `memo` varchar(45) DEFAULT NULL,
  `at_create` datetime DEFAULT NULL,
  `at_update` datetime DEFAULT NULL,
  `random_key` varchar(45) DEFAULT NULL,
  `other_status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_unique` (`fund_id`,`para_id`,`who`,`extrinsic_index`,`block_timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
         '''.format(cls.TableNameOfMysql())

    # 这里的字段和顺序如果更新，那么 getInsertSqlValues 方法的顺序也必须更新
    # TODO::之后调整更新需要同步更新其他方法的问题
    def getInsertSqlTemplate ( self , table_name ):
        return '''
        INSERT INTO {}
(`fund_id`, `para_id`, `who`, `contributed`, `contributing`, `block_num`, `block_timestamp`, `extrinsic_index`, `status`, `memo`, `at_create`, `at_update`, `random_key`) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
ON DUPLICATE KEY UPDATE 
`contributed`=%s, 
`contributing`= %s, 
`block_num`= %s, 
`status`= %s, 
`memo`= %s, 
`at_update`= %s,
`random_key`= %s ;
        '''.format(table_name)

    def getInsertSqlValues(self, time_zone) :
        return [
            self['fund_id'],
            self['para_id'],
            self['who'],
            self['contributed'],
            self['contributing'],
            self['block_num'],
            self['block_timestamp'],
            self['extrinsic_index'],
            self['status'],
            self['memo'],
            self.getCurrentTime(time_zone),
            self.getCurrentTime(time_zone),
            self['random_key'],
            #----- update
            self['contributed'],
            self['contributing'],
            self['block_num'],
            self['status'],
            self['memo'],
            self.getCurrentTime(time_zone),
            self['random_key'],
        ]

    # 获取当前系统时间
    def getCurrentTime(self, time_zone):
        '''
        获取当前系统时间
        '''
        return datetime.datetime.now(pytz.timezone(time_zone)).strftime('%Y-%m-%d %H:%M:%S')



