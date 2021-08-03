# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from crowdloan_contribute.items import ContributorItem, ExtrinsicItem

class CrowdloanContributePipeline:

    @classmethod
    def from_crawler(cls, crawler):
        # 初始化类参数
        cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", 'default_none')
        cls.HOST = crawler.settings.get("MYSQL_HOST", 'default_none')
        cls.PORT = crawler.settings.get("MYSQL_PORT", 3306)
        cls.USER = crawler.settings.get("MYSQL_USER", 'default_none')
        cls.PASSWD = crawler.settings.get("MYSQL_PASSWORD", 'default_none')
        # 新增一个时区设置，并且增加默认时区
        cls.TIMEZONE = crawler.settings.get("TIMEZONE", 'Asia/Shanghai')
        return cls()

    # 爬虫程序管道启动时
    def open_spider(self, spider):

        # print(self.MYSQL_DB_NAME, self.HOST, self.PORT, self.USER, self.PASSWD)
        self.dbconn = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWD, database=self.MYSQL_DB_NAME,charset='utf8')
        self.dbcursor = self.dbconn.cursor()

        # 进行数据表的创建，如果数据表不存在就进行创建
        self.createScrapyTable(ContributorItem.TableSchemeOfMysql())
        self.createScrapyTable(ExtrinsicItem.TableSchemeOfMysql())


    def close_spider(self, spider):
        '''
        1、关闭数据库游标对象 dbcursor
        2、关闭数据库对象 dbconn
        '''
        self.dbcursor.close()
        self.dbconn.close()

    def process_item(self, item, spider):
        if isinstance(item,  ContributorItem):
            # 执行数据插入, 表名称，Item 对象
            self.intoDb(ContributorItem.TableNameOfMysql(), item)
            return item
        elif isinstance(item, ExtrinsicItem):
            self.intoDb(ExtrinsicItem.TableNameOfMysql(), item)
            return item

        # print(item)
        # print("-----------")
        # return item

    # 创建数据表
    def createScrapyTable(self, create_sql):
        count = self.dbcursor.execute(create_sql)
        self.dbconn.commit()

    def intoDb(self, table_name, item):
        # 插入后返回受影响的行数，如果唯一索引存在则执行更新操作
        sql_template = item.getInsertSqlTemplate(table_name)
        sql_into_values = item.getInsertSqlValues(self.TIMEZONE)
        count = self.dbcursor.execute(sql_template,
                                      sql_into_values)
        # 打印受影响的行数
        self.dbconn.commit()
        print("Insert result is : {}".format(count))