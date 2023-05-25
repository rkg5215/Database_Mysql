import mysql.connector as c
con = c.connect(host="localhost",
                user="root",
                passwd="Batman",
                database="test")
if con.is_connected():
  print("Successfully Connected....")

cursor = con.cursor()
while True:
    code = int(input("Enter Code: "))
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))
    query = "Insert into emp values({},'{}',{})".format(code, name, salary)
    cursor.execute(query)
    con.commit()
    print("Data Inserted Successfully..")
    x=int(input("1-> For Data Entry\n2->For Exit\n Enter Choice: "))
    if x==2:
        break;
