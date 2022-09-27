# insert the data inside database
import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "password@123")
cursor = mydb.cursor()
s = "insert into madhu1234.madhu1234details values(6947 , 'Madhu Priya' , 'madhu.priya@klh.edu.in' , 100, 20)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
# after inserting the data in databases basically you need to commit the changes
mydb.commit()
cursor.execute("select * from madhu1234.madhu1234details")
for i in cursor.fetchall():
    print(i)