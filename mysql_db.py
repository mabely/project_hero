import mysql.connector
import mysql

connect_db = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd='baseTime2o'
)

c = connect_db.cursor()

c.execute('CREATE DATABASE saved_properties')
c.execute('SHOW DATABASES')

for x in c:
    print(x)