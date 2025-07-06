# Menggunakan standar library

import datetime

data_waktu = datetime.datetime.today() # / .now
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"bulan : {data_waktu.strftime('%b')}")
print(f"tanggal : {data_waktu.day}")
print(f"hari : {data_waktu.strftime('%A')}")

from collections import Counter
data = ['a','b','c','d','g','r','a','c','a','b']

# count = 0
# for i in data:
#   if i == 'a':
#     count += 1
    
# print(f"banyak huruf a : {count}")

data_count = Counter(data)
print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah c = {data_count['c']}")

import io 
file = io.open("file_text.txt",'r')
print(file.read())



























