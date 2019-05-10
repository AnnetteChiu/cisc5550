import sqlite3

sqlite_db = sqlite3.connect("todolist.db")
# res = sqlite_db.execute("""CREATE TABLE users (
#    ID INTEGER PRIMARY KEY AUTOINCREMENT,
#    NAME           TEXT      NOT NULL,
#    PW           TEXT       NOT NULL
# );""")
#
# res = sqlite_db.execute("""CREATE TABLE entries (
#    ID INTEGER NOT NULL,
#    what_to_do           TEXT      NOT NULL,
#    due_date           TEXT       NOT NULL,
#    status           TEXT       NOT NULL
# );""")
#
#
#
# # res = sqlite_db.execute("SELECT name FROM sqlite_master WHERE type='table';")
# res = sqlite_db.execute("""INSERT INTO  users (NAME, PW)
#                         values ('test1', '1');""")
# res = sqlite_db.execute("""INSERT INTO  users (NAME, PW)
#                         values ('test2', '2');""")

# res = sqlite_db.execute("""select NAME from users where ID = 1;""")
# sqlite_db.commit()
# print(list(res))
#
# sqlite_db.close();

import socket

# 查看当前主机名
print('当前主机名称为 : ' + socket.gethostname())

# 根据主机名称获取当前IP
print('当前主机的IP为: ' + socket.gethostbyname(socket.gethostname()))




