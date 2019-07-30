#!/bin/bash
a=$[RANDOM%101]		#随机值
k=0				#统计输入次数
b=0				#用于定义域左边界
c=100			#用于定义域右边界

while :
do
  read -p "请输入一个($b-$c)的数:" n
  let k++
  s=0

  if [ -z  $n ];then
    echo "请输入一个数字"
    continue
  fi

   for i in {1..100}
   do
    if [ $n == $i ];then
      break
    else
      let s++
    fi
   done

  if [ $s == 100 ];then
   echo "请输入一个数字"
   continue
  elif [ $n -ge $c ] || [ $n -le $b ];then
   echo "你给的数不在范围内"
  elif [ $n -eq $a ];then
   echo "你猜对了，猜了$k次"
   exit
  elif [ $n -gt $a ];then
   echo "猜大了"
   c=$n
  else
   echo "猜小了"
   b=$n
  fi
done

