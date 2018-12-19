import tomd
import re
import requests
from lxml import etree
from html.parser import HTMLParser


a = requests.get("https://loj.ac/problem/1")
tree = etree.HTML(a.content)
s = tree.xpath("//div[@class='row'][2]//p")[0]
d = HTMLParser().unescape(etree.tostring(s).decode())
md = tomd.Tomd(d).markdown
q = re.sub(re.compile("(<math>.+?</math>)", re.S), "", md)

print(q)