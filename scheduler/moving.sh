#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping moving at" $(date)> /tmp/test.log
cd /root/alterre/alterre.org/robot
/usr/local/bin/scrapy crawl ouicar
/usr/local/bin/scrapy crawl drivy
/usr/local/bin/scrapy crawl jelouemoncampingcar
/usr/local/bin/scrapy crawl wikicampers
/usr/local/bin/scrapy crawl bandbike
/usr/local/bin/scrapy crawl elouevelo
echo "finish scraping moving at" $(date)> /tmp/test.log
