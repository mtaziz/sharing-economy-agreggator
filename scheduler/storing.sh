#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping storing at" $(date)> /tmp/test.log
cd /root/alterre.org/robot
/usr/local/bin/scrapy crawl jestocke
/usr/local/bin/scrapy crawl ouistock
/usr/local/bin/scrapy crawl costockage

echo "finish scraping storing at" $(date)> /tmp/test.log
