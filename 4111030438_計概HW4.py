# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:28:41 2023

@author: User
"""

import sqlite3

conn = sqlite3.connect('BBQ.db')

cursor = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS meat
             (id INTEGER PRIMARY KEY,
              name TEXT,
              price INTEGER,
              quantity INTEGER)''')

cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('chicken', 30, 5)" )
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('beef', 55, 10) ")
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('pork', 40, 15)" )

conn.commit()

conn.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")


conn.execute("UPDATE meat SET quantity = 30 WHERE name = 'chicken'")


conn.execute("DELETE FROM meat WHERE price = 40")

conn.commit()

cursor = conn.execute("SELECT * FROM meat")
for row in cursor:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print("Price = ", row[2])
    print("Quantity = ", row[3])
    print("\n")
