import sqlite3

connect = sqltie3.connect('example.db')

c = cunnect.cursor()

# ASC increase

# DESC Decrease

c.execute('SELECT rowid, * FROM TBALE_NAME ORDER BY rowid DESC')

connect.commit()
connect.close()