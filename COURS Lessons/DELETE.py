import sqlite3

connect = sqlite3.connect()

c = connect.cursor()

c.execute("DELETE FROM TABLE_NAME WHERE ....")


connect.commit()
connect.close()