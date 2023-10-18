# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:28:41 2023

@author: User
"""

import sqlite3

conn = sqlite3.connect('BBQ.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS meat
             (id INTEGER PRIMARY KEY,
              name TEXT,
              price INTEGER,
              quantity INTEGER)''')

cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('chicken', 30, 5)" )
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('beef', 55, 10) ")
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('pork', 40, 15)" )

conn.commit()

cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()

print("目前表格資料:")
for BBQ in meat:
    print(BBQ)
    
conn.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")
conn.execute("UPDATE meat SET quantity = 30 WHERE name = 'chicken'")

conn.commit()

# 重新獲取最新的資料
cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()

print("更新後表格資料:")
for BBQ in meat:
    print(BBQ)

conn.execute("DELETE FROM meat WHERE price = 40")

conn.commit()

# 重新獲取最新的資料
cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()

print("刪除後表格資料:")
for BBQ in meat:
    print(BBQ)

cursor.close()
conn.close()


