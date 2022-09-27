import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "password@123")
cursor = mydb.cursor()
cursor.execute("select employee_id , emp_mailid from madhu1234.madhu1234details")
# for i in cursor.fetchall():
#     print(i)

# o/p is in the form of tuple
#  how to print the data in form of list?
l = []
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))

# fetch the data
# push the data
# access the data
# data dump operation