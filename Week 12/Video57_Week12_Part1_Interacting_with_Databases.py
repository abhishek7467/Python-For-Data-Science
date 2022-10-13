'''             Interacting with Database             '''

import sqlite3

from cv2 import VideoWriter
# step 1 --> COnnect to the database 

con = sqlite3.connect('test.db')

# step --> Create a cursor object 

cursorObj = con.cursor()


# Step --> 3 Use the execute method to run SQL query
# In this example we are going to create a table

cursorObj.execute('CREATE TABLE IF NOT EXISTS student(rollno INTEGER, name TEXT, gpa REAL)')

cursorObj.execute('SELECT * FROM student')

cursorObj.execute('INSERT INTO student values(101,"ABHISHEK",9.0)')
print(cursorObj.execute('SELECT * FROM student'))

cursorObj.execute('SELECT * FROM student')

def insert(r, n, g):
    con=sqlite3.connect('test.db')
    cursorObj=con.cursor()
    cursorObj.execute('INSERT INTO student values(?,?,?)',(r,n,g))
    con.commit()
    con.close()
insert(102,'Abhishek',8.9)

def create_table():
    con=sqlite3.connect('test.db')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS student(rollno INTEGER, name TEXT, gpa REAL)')
    con.commit()
    con.close()

create_table()

# Data retreval 
def view():
    conn = sqlite3.connect('test.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM student')
    rows = cur.fetchall()
    print(rows)
    conn.close()
    return rows

print(view())
insert(103,'Mahesh',9.89)
print(view())






