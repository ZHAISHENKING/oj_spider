"""
对比输出未爬取的文件
"""
import json

st = "/Users/mac/Desktop/"

with open(st+"all.txt", "r") as f:
    a=f.read()
a=json.loads(a)

with open(st+"c.txt", "r") as f:
    b=f.read()
b=json.loads(b)

c=[i for i in a if i not in b]

with open(st+"b.txt", "w") as f:
    f.write(str(c))
print("ok")
