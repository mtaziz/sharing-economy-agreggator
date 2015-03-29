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
scrapy crawl supermarmite -o supermarmite_`date +%Y-%m-%d-%H-%M`.json
scrapy crawl meetup -o meetup_`date +%Y-%m-%d-%H-%M`.json
scrapy crawl zilok -o zilok_`date +%Y-%m-%d-%H-%M`.json
scrapy crawl airbnb -o airbnb_`date +%Y-%m-%d-%H-%M`.json
scrapy crawl wimdu -o wimdu_`date +%Y-%m-%d-%H-%M`.json
scrapy crawl sejourning -o sejourning_`date +%Y-%m-%d-%H-%M`.json
scrapy crawl cohebergement 
scrapy crawl elouehebergement
scrapy crawl owlcamp
mysqldump -uroot -plifemaker1989 test ads > ads_`date +%Y-%m-%d-%H-%M`.sql
zip ads_`date +%Y-%m-%d-%H-%M`.sql.zip ads_`date +%Y-%m-%d-%H-%M`.sql 
