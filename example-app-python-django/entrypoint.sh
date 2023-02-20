#!/bin/sh
# wait-for-postgres.sh


# until mysql -u $DB_USER -h $DB_HOST -D $DB_NAME -p $DB_PASSWORD -e ";" ; do
#        echo "Can't connect " 
#        sleep 5
# done
# echo "Mysql is up - executing command"

# until psql "postgresql://host.docker.internal@roach1:26257?sslmode=disable" -c '\q' >/dev/null 2>&1; do
#     echo "PostgreSQL is unavailable - sleeping"
#     sleep 5
# done

sleep 10

echo "PostgreSQL is up - executing command"

python ./cockroach_example/manage.py runserver 0.0.0.0:8080

sleep infinity