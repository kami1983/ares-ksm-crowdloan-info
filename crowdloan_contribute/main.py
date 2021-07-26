from scrapy.cmdline import execute

import sys
import os

# print("#########")
# print( os.path.dirname(os.path.abspath(__file__)) )
# 目的是把当前的目录加入环境变量
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 执行爬虫
execute(["scrapy", "crawl", "subscan"])
