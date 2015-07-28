#!/bin/bash
echo $(date)  > /tmp/test.log
echo "start preprocessing stored data  at" $(date)> /tmp/test.log
mysql --xml -uroot -plifemaker1989 alterrefront -e "UPDATE ads SET subcategory='sport' WHERE title LIKE '%velo%appart%';"

echo "finish preprocessing stored data at" $(date)> /tmp/test.log
