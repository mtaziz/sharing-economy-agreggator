#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping parking at" $(date)> /tmp/test.log
cd /root/alterre/alterre.org/robot
/usr/local/bin/scrapy crawl prendsmaplace
/usr/local/bin/scrapy crawl monsieurparking
/usr/local/bin/scrapy crawl parkadom

echo "finish scraping parking at" $(date)> /tmp/test.log