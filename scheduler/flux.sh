#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start generating dreamville xml flux  at" $(date)> /tmp/test.log
cd /root/alterre/alterre.org/api/alterre
/usr/local/bin/scrapy crawl dreamville -o dreamville.xml

echo "finish dreamville xml file at" $(date)> /tmp/test.log
