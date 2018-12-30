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
    name = 'problem'
    allowed_domains = ['loj.ac']
    start_urls = ['https://loj.ac/problem']

    def parse(self, response):
        """处理问题列表"""
        a=[10226, 10233, 10236, 10195, 10204, 10207, 10210, 10124, 10125, 10126, 10139, 10140, 10142, 10146, 10073, 10079, 10080, 10089, 10107, 10113, 10118, 10025, 10026, 10032, 10033, 10039, 10040, 10044, 10055, 10071, 6340, 6200, 6201, 6116, 6135, 2950, 2655, 2656, 2568, 2569, 2570, 2571, 2572, 2573, 2577, 2579, 2581, 2582, 2585, 2586, 2587, 2590, 2594, 2466, 2467, 2469, 2470, 2472, 2474, 2475, 2476, 2478, 2479, 2480, 2481, 2482, 2373, 2383, 2385, 2386, 2387, 2391, 2392, 2393, 2395, 2396, 2397, 2289, 2302, 2307, 2316, 2258, 2155, 2156, 9]
        print(len(a))
        for i in a:
            r = Request('https://loj.ac/problem/%d/testdata/download' % i, callback=self.parse_post)
            r.meta["num"] = i
            yield r

    def parse_post(self, response):
        i = response.meta["num"]

        filename = '/Users/mac/Desktop/rename/package/problem%d.zip' % i
        r = requests.get('https://loj.ac/problem/%d/testdata/download' % i)
        with open(filename, "wb") as f:
            f.write(r.content)
        yield
