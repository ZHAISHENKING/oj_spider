#!/bin/sh
echo "输出已爬取的问题"
rm c.txt b.txt

for i in rename/package/*
do
echo -n "$i," >> c.txt
done

