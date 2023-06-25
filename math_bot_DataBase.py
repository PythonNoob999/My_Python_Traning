# importing the SQLite3 Module built-in python
import sqlite3

# making a connection between the python script and the database file
con = sqlite3.connect("math_bot_database.db")
# Createing DataBase Cursor to Execute MYSQL Code 
# Cursor behave like the Terminal For you database Management
c = con.cursor()

# NOTE*****
"""
You need to run the command "CREATE TABLE table_name (table, inputs)" Through Cursor
Example:
c.execute('CREATE TABLE users (
    id text,
    salary integer)
)
Once you run this code you Maked the DataBase Successfully and don't need it any more
"""

# A func to add new members
def add_member(id, salary):
    # making another Connection to the DB
    con = sqlite3.connect("math_bot_database.db")
    c = con.cursor()
    # This command get all of DB entrys
    c.execute("SELECT * FROM member")
    # this command search for all of the DB elements
    items = c.fetchall()
    # printing every single column in the DB
    for item in items:
       # checking if user already exist in our DB to not duplicate users
        if id in item:
            return "User Exists"
        elif id not in item:
            # Inserting the User id and Salary in a new column
            c.execute('INSERT INTO member VALUES (?, ?)', (id, salary))
            # commitng the changes on the DB
            con.commit()
# Updateing User Salary
def update_salary(id, new_salary):
    con = sqlite3.connect("math_bot_database.db")
    c = con.cursor()
    c.execute("SELECT * FROM member")
    items = c.fetchall()
    for item in items:
        # checking if the user id is not in our DB or in another words "Checking if user Exists or not"
        if id not in item:
            return "User Does Not Exsist"
        # if user is in our DB
        elif id in item:
            # Update the salary To the user with the ID that have been given to us
            c.execute(f"UPDATE member SET salaey = '{new_salary}' WHERE id = '{id}'")
            con.commit()
          
# Getting the Current User salary
def get_last_salary(id):
    con = sqlite3.connect("math_bot_database.db")
    c = con.cursor()
    # Selecting the Salary from our user ID
    c.execute(f"SELECT salary FROM member WHERE id = '{id}' ")
    items = c.fetchall()
    # Return Only the Salary
    for item in items:
        return item[0]
