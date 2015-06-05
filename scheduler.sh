#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start scraping at" $(date)> /tmp/test.log
cd /root/alterre/alterre.org/robot
/usr/local/bin/scrapy crawl zilok
/usr/local/bin/scrapy crawl eloue
/usr/local/bin/scrapy crawl airbnb
/usr/local/bin/scrapy crawl bandbike
/usr/local/bin/scrapy crawl boaterfly
/usr/local/bin/scrapy crawl prendsmaplace
/usr/local/bin/scrapy crawl pretersonjardin
/usr/local/bin/scrapy crawl chambrealouer
/usr/local/bin/scrapy crawl cavientdujardin
/usr/local/bin/scrapy crawl cohebergement
/usr/local/bin/scrapy crawl cookening
/usr/local/bin/scrapy crawl costockage
/usr/local/bin/scrapy crawl drivy
/usr/local/bin/scrapy crawl eloue
/usr/local/bin/scrapy crawl elouesport
/usr/local/bin/scrapy crawl elouemoto
/usr/local/bin/scrapy crawl elouevelo
/usr/local/bin/scrapy crawl elouehebergement
/usr/local/bin/scrapy crawl jelouemoncampingcar
/usr/local/bin/scrapy crawl jestocke
/usr/local/bin/scrapy crawl housetrip
/usr/local/bin/scrapy crawl meetup
/usr/local/bin/scrapy crawl meetnsport

echo "finish scraping" > /tmp/test.log
~                                        