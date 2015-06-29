#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping daily at" $(date)> /tmp/test.log
cd /root/alterre/alterre.org/robot
/usr/local/bin/scrapy crawl eloue
/usr/local/bin/scrapy crawl zilok
/usr/local/bin/scrapy crawl bricolib
echo "finish scraping daily at" $(date)> /tmp/test.log
