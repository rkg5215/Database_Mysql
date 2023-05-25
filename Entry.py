import mysql.connector as c
con = c.connect(host="localhost",
                user="root",
                passwd="Batman",
                database="noida")
if con.is_connected():
  print("Successfully Connected....")

cursor = con.cursor()
while True:
    id = int(input("Enter ID: "))
    firstname = input("Enter Firstname: ")
    lastname = input("Enter Lastname: ")
    query = "Insert into emp values({},'{}','{}')".format(id, firstname, lastname)
    cursor.execute(query)
    con.commit()
    print("Data Inserted Successfully..")
    x=int(input("1-> For Data Entry\n2->For Exits\n Enter Choice: "))
    if x==2:
        break;
