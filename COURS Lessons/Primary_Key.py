import sqlite3 

# connect the database
connect = sqlite3.connect("costumer.db")

# create the cursor
cursor = connect.cursor()

# you don't have to create the id cause he came by default in sqlite3
cursor.execute('SELECT rowid, * FROM customers')

# stor all the data in items
items = cursor.fetchall()

# now we can see every itsm's id
for item in items:
    print(item)

# PRIMARY KEY : a unique id each identifies each row in a database table