#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping eating at" $(date)> /tmp/test.log
cd /root/alterre/alterre.org/robot
/usr/local/bin/scrapy crawl vizeat
/usr/local/bin/scrapy crawl cookening
/usr/local/bin/scrapy crawl plantezcheznous
echo "finish scraping eating at" $(date)> /tmp/test.log
