#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping housing at" $(date)> /tmp/test.log
cd /root/alterre/alterre.org/robot
/usr/local/bin/scrapy crawl bedycasa
/usr/local/bin/scrapy crawl owlcamp
/usr/local/bin/scrapy crawl sejourning
/usr/local/bin/scrapy crawl housetrip
/usr/local/bin/scrapy crawl airbnb
/usr/local/bin/scrapy crawl chambrealouer

echo "finish scraping housing at" $(date)> /tmp/test.log
