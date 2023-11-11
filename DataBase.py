import sqlite3

connection = sqlite3.connect("itstep.sl3", 2)

cur = connection.cursor()
#cur.execute("SELECT rowid, user_name, email FROM users;")
cur.execute("DELETE FROM users where rowid=5;")
connection.commit()

#res = cur.fetchall()
#print(res)
# print(connection)
# print(cur)

connection.close()

