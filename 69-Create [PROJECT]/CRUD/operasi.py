from . import database,util
from .util import random_string
import time

def create_first_data():
   penulis = input("Penulis: ")
   judul = input("Judul: ")
   while(True):
      try:
         tahun = int(input("Tahun\t: "))
         if len(str(tahun)) == 4:
            break
         else: print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)\n")
      except:
         print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)\n")
   
   data = database.TEMPLATE.copy()
   
   data["pk"] = random_string(6)
   data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
   data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
   data["judul"] = judul + database.TEMPLATE["judul"][len(judul)]
   data["tahun"] = str(tahun) 
   
   data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
   
   try:
      with open(database.DB_NAME,"w",encoding="utf-8") as file:
         file.write(data_str)
   except:
      print("Waduh Gak Bisa Nih!!!")
   
def read():
   try:
      with open(database.DB_NAME,"r") as file:
         content = file.readlines()
         return content
   except:
      print("Membaca database error")
      return False
   
def create(penulis,judul,tahun):
   data = database.TEMPLATE.copy()
   
   data["pk"] = random_string(6)
   data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
   data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
   data["judul"] = judul + database.TEMPLATE["judul"][len(judul)]
   data["tahun"] = str(tahun)
   
   data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
   
   try:
      with open(database.DB_NAME,"a",encoding="utf-8") as file:
         file.write(data_str)
   except:
      print("Data sulit ditambahkan bang, pusyinggggg")













   