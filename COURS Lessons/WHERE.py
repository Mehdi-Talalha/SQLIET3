import sqlite3

# Connect to the database
connect = sqlite3.connect('data.db')

# create a cursor
c = connect.cursor()

# for comaring TEXT
c.execute("SELECT name FROM user WHERE name like 'M%'") #% means 'somethin' 
c.execute("SELECT * FROM user WHERE 1 <= 2") 

# Printing Results
elems = c.fetchall()

for elem in elems:
    print(elem)


connect.commit()

connect.close()