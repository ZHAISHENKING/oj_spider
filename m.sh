#!/bin/sh
for i in *
do
k=$i
echo $i
if [ "$i" -le 2000 ]
then
    mv $i ../../a
elif [ "$i" -le 5000 ]
then
    mv $i ../../b
elif [ "$i" -le 13000 ]
then
    mv $i ../../c
else
    echo "ok"
fi

done
