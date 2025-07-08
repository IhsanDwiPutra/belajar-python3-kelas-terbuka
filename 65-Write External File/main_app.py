# Write External file 

# 1. mode write 
# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa atau overwrite isinya
with open("data_1.txt",mode='w',encoding="utf-8") as file:
  file.write("Gus Markus")

with open("data_1.txt",mode='w',encoding="utf-8") as file:
  file.write("Ketimpa jadinya bos")

# 2. mode append  
with open("data_2.txt",mode='w',encoding="utf-8") as file:
  file.write("Agus Markucus\n")
  
with open("data_2.txt",mode='a',encoding="utf-8") as file:
  file.write("Marko Mar\n")
  
with open("data_2.txt",mode='a',encoding="utf-8") as file:
  file.write("tambah lagi dengan append")

# 3. mode r+
with open("data_3.txt",mode='w',encoding="utf-8") as file:
  file.write("data ke 3\n")

with open("data_3.txt",mode='r+',encoding="utf-8") as file:
  file.write("baris ke-1\n")
  file.write("baris ke-2\n")
  file.write("baris ke-3\n")
  
with open("data_3.txt",mode='r+',encoding="utf-8") as file:
  data = file.read()
  print(data)
  
with open("data_3.txt",mode="r+",encoding="utf-8") as file:
  file.write("Agus Markucus\n") # menimpa isi text sesuai dengan panjang data















