#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping parking at" $(date)> /tmp/test.log
cd /root/alterre.org/robot
/usr/local/bin/scrapy crawl prendsmaplace
/usr/local/bin/scrapy crawl monsieurparking
/usr/local/bin/scrapy crawl parkadom
/usr/local/bin/scrapy crawl mobypark
/usr/local/bin/scrapy crawl sharedparking
echo "finish scraping parking at" $(date)> /tmp/test.log
