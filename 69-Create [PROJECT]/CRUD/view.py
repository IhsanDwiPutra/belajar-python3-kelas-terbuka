from . import operasi

def read_console():
   data_file = operasi.read()
   index = "No"
   judul = "Judul"
   penulis = "Penulis"
   tahun = "Tahun"
   
   # header   
   print("\n"+100*'=')
   print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
   print(100*'-')
   
   # data 
   for index,data in enumerate(data_file):
      data_break = data.split(",")
      pk = data_break[0]
      date_add = data_break[1]
      penulis = data_break[2]
      judul = data_break[3]
      tahun = data_break[4] 
      print(f"{index+1:4} | {judul.title():40} | {penulis.title():.40} | {tahun:4}",end="")
      
   
   # footer
   print(100*'='+"\n")

def create_console():
   print("\n\n"+100*"=")
   print("Silahkan tambah data buku\n")
   penulis = input("Penulis\t: ")
   judul = input("Judul\t: ")
   
   while(True):
      try:
         tahun = int(input("Tahun\t: "))
         if len(str(tahun)) == 4:
            break
         else: print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)\n")
      except:
         print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)\n")

   operasi.create(penulis,judul,tahun)
   print("\nBerikut adalah data baru anda")
   read_console()
















