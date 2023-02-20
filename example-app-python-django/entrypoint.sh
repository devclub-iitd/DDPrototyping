#!/bin/sh
# wait-for-postgres.sh


# until mysql -u $DB_USER -h $DB_HOST -D $DB_NAME -p $DB_PASSWORD -e ";" ; do
#        echo "Can't connect " 
#        sleep 5
# done
# echo "Mysql is up - executing command"

until psql -U $DB_USER -h $DB_HOST -d $DB_NAME -p $DB_PORT -c "SELECT 1" >/dev/null 2>&1; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 5
done

echo "PostgreSQL is up - executing command"

python ./cockroach_example/manage.py runserver 0.0.0.0:8080

sleep infinity