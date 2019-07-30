#!/bin/bash
#本脚是用来查找符合条件的文档，主要是根据文档中含有的关键字进行查找。以搜索/etc目录为例，查找欢迎界面的文件。
for i in $(find /etc/ -type f)
do 
	cat $i | grep "I  am  Virtual Host ! ! !" &> /dev/null
	if [ $? -eq 0 ];then 
		echo $i
		break  
	else
		continue
	fi
	
done

