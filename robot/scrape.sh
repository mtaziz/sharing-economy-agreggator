#!/bin/bash

source $WORKON_HOME/scrapper/bin/activate
cd /home/mohamed/side_projects/alterre.org/robot

scrapy crawl airbnb 
scrapy crawl plantezcheznous
scrapy crawl bandbike
scrapy crawl boaterfly
scrapy crawl prendsmaplace
scrapy crawl pretersonjardin
scrapy crawl chambrealouer
scrapy crawl cavientdujardin
scrapy crawl cohebergement 
scrapy crawl cookening
scrapy crawl costockage
scrapy crawl drivy 
scrapy crawl eloue
scrapy crawl elouesport
scrapy crawl elouemoto
scrapy crawl elouevelo
scrapy crawl elouehebergement

scrapy crawl jelouemoncampingcar
scrapy crawl jestocke
scrapy crawl housetrip
scrapy crawl meetup 
scrapy crawl meetnsport
scrapy crawl monsieurparking
scrapy crawl parkadom

scrapy crawl ouicar
scrapy crawl ouistock
scrapy crawl owlcamp

scrapy crawl sailsharing 
scrapy crawl samboat
scrapy crawl sejourning 
scrapy crawl supermarmite 
scrapy crawl zealguide

scrapy crawl videdressing
scrapy crawl zilok 
scrapy crawl zilokmanutention
scrapy crawl wimdu 