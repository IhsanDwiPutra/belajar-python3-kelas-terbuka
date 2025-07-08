# Exception Error Try and Except 

# file = open("data.txt",mode='r') # jika file tidak ada maka akan terjadi runtime error

# exception akan terjadi saat program menglamai error saat runtime

# contoh sederhana untuk menangkap exception 
from math import nan

# contoh sederhana
# data_input = int(input("Masukkan angka: "))
# hasil = nan
# try:
#   hasil = 10/data_input
# except:
#   print("input tidak boleh 0")
# print(f"hasil bagi = {hasil}")

# while True:
#   angka = int(input("Masukkan angka pembagi: "))
#   hasil = nan
#   try:
#     hasil = 10/angka
#     print(f"hasiil = {hasil}")
#     is_done = input("Lanjutkan (y/n) ?: ")
#     if is_done == 'n':
#       break 
#   except:
#     print("pembagi nol, silahkan masukan input lagi!")
    
# print("Akhir dari pogram 1")

# contoh aplikasi untuk membuat file data.txt
try:
  with open("data.txt",'r') as file:
    print(file.read())
except:
  print("file data.txt tidak ditemukan, membuat file baru")
  with open("data.txt",'w',encoding="utf-8") as file:
    file.write("file baru")
    
print("akhir dari program 2")














