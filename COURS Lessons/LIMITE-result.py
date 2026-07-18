import sqlite3

connect = sqlite3.connect('example.db')

c = connect.cursor()

c.execute('SELECT * FROM TABLE_NAME LIMIT 2 ORDER BY rowid DESC')

connect.commit()
connect.close()