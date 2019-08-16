#!/bin/bash
date=`date +%Y%m%d`
logpath=/usr/local/nginx/logs
mv $logpath/access.log $logpath/access-$date.log
mv $logpath/error.log $logpath/error-$date.log
kill -USR1 $(cat $logpath/nginx.pid)

# 然后再添加定时任务：
# [root@proxy ~]# crontab -e
# 03 03 * * 5  /usr/local/nginx/logbak.sh
