# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:06:16 2023

@author: User
"""

import os
import time
os.mkdir("CS")

file = os.path.join("CS", "homework.txt")

with open("homework.txt","w") as file:
    content = "4111030438_許琮彥"
    file.write(content)

with open("homework.txt","r") as file:
    content= file.read()
    print(f"文件內容： {content} ")

file_size = os.path.getsize("homework.txt")
print(f"檔案大小：{file_size}字節")

modification_time = os.path.getmtime("homework.txt")
print(f"最後修改時間：{modification_time}")

new_access_time = time.time()
print(f"最後訪問時間：{new_access_time}")

os.remove("homework.txt")
print("已刪除文件")

os.rmdir("CS")
print("已刪除目錄")

