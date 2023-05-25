# Connection with MYSQL Database
import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="Batman", database="test")
if con.is_connected():
    print("Successfully Connected....")
else:
    print("Connection Issue....")

