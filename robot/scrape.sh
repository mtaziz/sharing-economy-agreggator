#!/bin/bash

source $WORKON_HOME/scrapper/bin/activate
cd /home/mohamed/side_projects/alterre.org/robot
scrapy crawl drivy 
scrapy crawl housetrip
scrapy crawl chambrealouer
scrapy crawl jelouemoncampingcar
scrapy crawl boaterfly
scrapy crawl jestocke
scrapy crawl ouicar
scrapy crawl sailsharing 
scrapy crawl ouistock
scrapy crawl eloue
scrapy crawl elouesport
scrapy crawl elouemoto
scrapy crawl supermarmite
scrapy crawl meetup
scrapy crawl zilok
scrapy crawl airbnb
scrapy crawl wimdu
scrapy crawl sejourning

mysqldump -uroot -plifemaker1989 test ads > ads_`date +%Y-%m-%d-%H-%M`.sql
