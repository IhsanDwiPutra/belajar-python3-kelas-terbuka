# read external file open dan with
## tutorial membaca file external

print(3*'=', " Membaca File txt " , 3*'=')
file = open("data.txt",mode='r')

# print(f"status read : {file.readable()}")
# print(f"status write : {file.writable()}")

## baca seluruh baris
# print(file.read())

## baca per baris
# print(file.readline(),end='') # baca baris pertama
# print(file.readline(),end='') # baca baris kedua

## baca semua baris sebagai list
# print(file.readlines(),end='')

print(f"apakah file sudah diclose : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")

## salah satu teknik membuka file di python
print(3*'=', " Membaca File txt dengan With " , 3*'=')
with open("data.txt",mode='r') as file:
  content = file.readline()
  print(content,end='')
  print(f"apakah file sudah di close : {file.closed}")
  
print(f"apakah file sudah di close : {file.closed}")


















