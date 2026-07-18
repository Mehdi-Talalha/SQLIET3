import sqlite3

# Connect to database
connect = sqlite3.connect("example.db")

# Create cursor
cursor = connect.cursor()

# Query the database
cursor.execute("SELECT * FROM TABLE_NAME")

# you can get the returned data via the reture value of cursor.fetchall()
items = cursor.fetchall()

for item in items:
    print(item)

# Commit changes
connect.commit()

# Close connection
connect.close()
