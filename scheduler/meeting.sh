#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping meeting at" $(date)> /tmp/test.log
cd /root/alterre/alterre.org/robot
/usr/local/bin/scrapy crawl meetup
echo "finish scraping meeting at" $(date)> /tmp/test.log
