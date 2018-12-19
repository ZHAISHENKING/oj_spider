# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
# from scrapy.shell import inspect_response
from scrapy_redis.spiders import RedisSpider
from oj.items import OjItem
import time, os
import requests
import re
# import tomd


class ProblemSpider(RedisSpider):
    name = 'problem'
    allowed_domains = ['loj.ac']
    redis_key = 'problem:start_urls'
    # start_urls = ['https://loj.ac/problem']

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(ProblemSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        """处理问题列表"""
        parents = response.xpath('//div[@class="ui main container"]')

        for parent in parents:
            post = OjItem()

            try:
                title = parent.xpath("//h1[@class='ui header']/text()").get().split(".", 1)
                post["number"] = title[0].split("#")[1]
                post['title'] = title[1]

                r = requests.get('https://loj.ac/problem/%d/testdata/download' % post["number"])
                filename = 'package/problem%d.zip' % post["number"]
                if not os.path.exists(os.path.split(filename)[0]):
                    # 目录不存在创建，makedirs可以创建多级目录
                    os.makedirs(os.path.split(filename)[0])
                with open(filename, 'wb') as fp:
                    fp.write(r.content)
                print(filename + "下载完毕")

                try:
                    post['desc'] = self.html2md(
                        parent.xpath("//div[@class='row'][2]//div[@class='ui bottom attached segment font-content']")[
                            0])
                except Exception:
                    post["desc"] = ""
                try:
                    post["input_desc"] = self.html2md(
                        parent.xpath("//div[@class='row'][3]//div[@class='ui bottom attached segment font-content']")[
                            0])
                except Exception:
                    post["input_desc"] = ""
                try:
                    post["output_desc"] = self.html2md(
                        parent.xpath("//div[@class='row'][4]//div[@class='ui bottom attached segment font-content']")[
                            0])
                except Exception:
                    post["output_desc"] = ""
                try:
                    post['example_input'] = self.html2md(
                        parent.xpath("//div[@class='ui existing segment'][1]/pre/code[@class='lang-plain']")[0])
                except Exception:
                    post['example_input'] = ""
                try:
                    post['example_output'] = self.html2md(
                        parent.xpath("//div[@class='ui existing segment'][2]/pre/code[@class='lang-plain']")[0])
                except Exception:
                    post["example_output"] = ""
                try:
                    post['tig'] = self.html2md(parent.xpath("//div[@class='row'][6]//p")[0])
                except Exception:
                    post['tig'] = ""

                cate = parent.xpath("//div[@id='show_tag_div']//text()")
                s = ""
                for i in cate:
                    s += i.get() + " "
                post["category"] = s
            except Exception as e:
                print(e)
            finally:
                yield post
                print(post)

    @staticmethod
    def html2md(s):

        # md = tomd.Tomd().markdown
        q = re.sub(re.compile("(<math>.+?</math>)", re.S), "", s.extract())
        while re.search(re.compile('</div>'),q):
            q = re.sub(re.compile("<div.*?>(.+?)</div>", re.S), "\\1", q)
        while re.search(re.compile('</p>'), q):
            q = re.sub(re.compile("<p.*?>(.+?)</p>", re.S), "\\1", q)
        while re.search(re.compile('</code>'), q):
            q = re.sub(re.compile("<code.*?>(.+?)</code>", re.S), "\\1", q)
        while re.search(re.compile("</span>"), q):
            q = re.sub(re.compile('(<span.*?>)(.*?)(</span>)', re.S), "\\2", q)

        return q
