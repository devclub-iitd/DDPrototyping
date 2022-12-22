import mysql.connector as mysql
import os

HOST = os.getenv('MYSQL_HOST', None)
USER = os.getenv('MYSQL_USER', None)
PASSWORD = os.getenv('MYSQL_PASSWORD', None)
DB = os.getenv('MYSQL_DB', None)


print("Service A: Environment variable are", USER, HOST, PASSWORD, DB)
mydb = mysql.connect(host = HOST, user = USER, port="3306", passwd = PASSWORD, database = DB)
mycursor = mydb.cursor()

tables = mycursor.execute("SHOW TABLES")

f=0
for x in tables:
    if x=="tableA":
        f = 1

if f==0:
    mycursor.execute("CREATE TABLE tableA(id int Primary Key, Value varchar(15))")

print("serviceA running and inserting values to",DB)

mycursor.execute("INSERT INTO tableA VALUES(1, 'data1')")
mycursor.execute("INSERT INTO tableA VALUES(2, 'data2')")

mycursor.execute("Select * from tableA")
data = mycursor.fetchall()
for x in data:
    print(x)

mydb.commit()

