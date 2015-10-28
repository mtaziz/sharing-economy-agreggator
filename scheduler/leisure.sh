#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping leisure at" $(date)> /tmp/test.log
cd /root/alterre.org/robot
/usr/local/bin/scrapy crawl elouesport
/usr/local/bin/scrapy crawl boaterfly
/usr/local/bin/scrapy crawl clickandboat
/usr/local/bin/scrapy crawl samboat

echo "finish scraping leisure at" $(date)> /tmp/test.log
