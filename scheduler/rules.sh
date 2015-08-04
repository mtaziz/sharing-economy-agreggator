#!/bin/bash
echo $(date)  > /tmp/scraper.log
echo "start preprocessing stored data  at" $(date)> /tmp/scraper.log
mysql  -uroot -plifemaker1989 alterrefront -e "UPDATE ads SET subcategory='sport' WHERE title LIKE '%velo%appart%';"
mysql -uroot -plifemaker1989 alterrefront -e "DELETE FROM ads WHERE title LIKE 'stage %';"
echo "finish preprocessing stored data at" $(date)> /tmp/scraper.log
