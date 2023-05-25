import mysql.connector as c
db = c.connect(host="localhost",
                   user="root",
                   passwd="Batman",
                   database="reg")
cur = db.cursor()
cur.execute("SELECT * FROM user")
result=cur.fetchall()
print(result)

for row in result:
    print(row)



