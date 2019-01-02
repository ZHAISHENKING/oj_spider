#!/bin/sh
rm c.txt b.txt

for i in rename/package/*
do
echo -n "$i," >> c.txt
done

