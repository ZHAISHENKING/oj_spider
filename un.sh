#! /bin/sh
for i in rename/package/*.zip
do
k=$i
s=${k%.zip*}
echo ${s#*problem*}
unzip $i -d rename/package/${s#*problem*}
done
