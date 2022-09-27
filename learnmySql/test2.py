# create a database
import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "password@123")
cursor = mydb.cursor()
# cursor.execute("create database madhu")
# cursor.execute("show databases")
# create a table
# s = cursor.execute("create table madhu.KLH(employee_id int(10) , employee_name varchar(20) , emp_mailid varchar(30) , emp_salary int(6) , emp_attandance int(3)")
# print(cursor.fetchall())

# s = "create table madhu1234.madhu1234details(employee_id int(10) , emp_name varchar(20) , emp_mailid varchar(30) , emp_salary int(6), emp_attandance int(3))"
# cursor.execute(s)
q2 = cursor.execute("select * from madhu1234.madhu1234details")
print(q2)

