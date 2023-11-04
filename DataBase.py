import sqlite3

connection = sqlite3.connect("itstep.sl3", 5)

cur = connection.cursor()

cur.execute("CREATE TABLE users(user_name TEXT); ")
connection.commit()


# print(connection)
# print(cur)

connection.close()

