# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class OjPipeline(object):

    # 蜘蛛开始爬取的时候自动调用
    def open_spider(self, spider):
        self.fp = open('/Users/mac/Desktop/rename/package', 'a+', encoding='utf-8')

    def close_spider(self, spider):
        self.fp.close()

    # 这是一个回调方法，是由引擎自动调用，引擎会把要存储的数据一个一个的通过item参数传递回来
    # spider就是回传数据给引擎的那个蜘蛛对象
    def process_item(self, item, spider):
        json_str = json.dumps(item, ensure_ascii=False, indent=4)
        self.fp.write(json_str + "," + '\n')
        return item
