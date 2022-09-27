import mysql.connector as conn
# pip install mysql-connector-python
mydb = conn.connect(host = "localhost", user = "root", passwd = "password@123") #establish communication
print(mydb) # print the object mydb
cursor = mydb.cursor() # create a cursor
cursor.execute("show databases") # execute the quaries
print(cursor.fetchall()) # show the executed quaries
# this is the 4 line of code which you need to write everytime you are going to establish the communication with database
