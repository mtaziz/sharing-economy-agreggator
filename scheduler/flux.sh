#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start generating dreamville xml flux  at" $(date)> /tmp/test.log
cd ../api/alterre
#touch dreamville.xml
mysql --xml -uroot -plifemaker1989 alterrefront -e "SELECT * FROM ads WHERE location LIKE '%rouen%'" > dreamville.xml

echo "finish dreamville xml file at" $(date)> /tmp/test.log
