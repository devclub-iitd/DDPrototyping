#!/bin/sh
# wait-for-postgres.sh


until mysql -u $MYSQL_USER -h $MYSQL_HOST -D $MYSQL_DB -p$MYSQL_PASSWORD -e ";" ; do
       echo "Can't connect " 
       sleep 5
done
echo "Mysql is up - executing command"

python serviceA.py

sleep infinity


