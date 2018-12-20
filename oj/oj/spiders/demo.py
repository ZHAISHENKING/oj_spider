
# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
# from scrapy.shell import inspect_response
from oj.items import OjItem
import time, os
import requests
import re
# import tomd


class ProblemSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['loj.ac']
    start_urls = ['https://loj.ac/problem']

    def parse(self, response):
        """处理问题列表"""
        a = [1,2,3,4,5,6,7,9]
        for i in a:
            url = "https://loj.ac/problem/%d" % i
            request = Request(url, callback=self.parse_post, dont_filter=True)
            request.meta["num"] = i
            yield request

    def parse_post(self, response):
        print(response.meta["num"])
        post = {}
        try:
            title = response.xpath("//h1[@class='ui header']/text()").get().split(".", 1)
            post["number"] = title[0].split("#")[1]
            post['title'] = title[1]
        except Exception:
            yield

        try:
            post['desc'] = self.html2md(
                response.xpath("//div[@class='row'][2]//div[@class='ui bottom attached segment font-content']")[
                    0])
        except Exception:
            post["desc"] = ""
        try:
            post["input_desc"] = self.html2md(
                response.xpath("//div[@class='row'][3]//div[@class='ui bottom attached segment font-content']")[
                    0])
        except Exception:
            post["input_desc"] = ""
        try:
            post["output_desc"] = self.html2md(
                response.xpath("//div[@class='row'][4]//div[@class='ui bottom attached segment font-content']")[
                    0])
        except Exception:
            post["output_desc"] = ""
        try:
            post['example_input'] = self.html2md(
                response.xpath("//div[@class='ui existing segment'][1]/pre/code[@class='lang-plain']")[0])
        except Exception:
            post['example_input'] = ""
        try:
            post['example_output'] = self.html2md(
                response.xpath("//div[@class='ui existing segment'][2]/pre/code[@class='lang-plain']")[0])
        except Exception:
            post["example_output"] = ""
        try:
            post['tig'] = self.html2md(response.xpath("//div[@class='row'][6]//p")[0])
        except Exception:
            post['tig'] = ""

        with open('oj.json', 'a+', encoding='utf-8') as f:
            json_str = json.dumps(post, ensure_ascii=False, indent=4)
            f.write(json_str + "," + '\n')
            f.close()
        yield



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
