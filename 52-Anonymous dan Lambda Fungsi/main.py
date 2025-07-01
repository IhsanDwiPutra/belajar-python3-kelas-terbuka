# anonymous dan lambda fungsi

# Lambda Function
def f_kuadrat(angka):
  return angka**2
  
print(f'hasil fungsi kuadrat = {f_kuadrat(3)}')

# kita coba dengan lambda 
kuadrat = lambda angka:angka**2
print(f'hasil lambda kuadrat = {kuadrat(5)}')

sapa = lambda nama:print(f'hai {nama} apa kabar')
nama = sapa('agus')

hasil = kuadrat(9)
print(hasil)

pangkat = lambda num,pow : num**pow
print(f'hasil lambda pangkat = {pangkat(5,3)}')

toples = lambda *args: print(args[0])
toples('hai')

## kegunaan apa bang?
# sorting untuk list
data_list = ['mikael','zamboy','bagas']
data_list.sort()
print(f'sorted list = {data_list}')

# sorting dai pakai panjang
def panjang_nama(nama):
  return len(nama)
  
data_list.sort(key=panjang_nama)
print(f'sorted list by panjang = {data_list}')

# sort pakai lambda 
data_list = ['xboy','salman','m']
data_list.sort(key=lambda nama:len(nama))
print(f'sorted list by lamdba = {data_list}')

# filter 
data_angka = [3,5,4,3,5,6,3,2,56,3,4,2,4,2,4]

def kurang_dari_lima(angka):
  return angka < 5
  
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(data_angka_baru)
data_angka_baru = list(filter(lambda x : x < 3,data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x : (x % 2 == 0), data_angka))
print(data_genap)

# kasus ganjil
data_angka = [157,3,5,4,3,5,6,3,2,56,3,4,2,4,2,4,111]
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x : (x % 3 == 0), data_angka))
print(data_3)

# anonymous fungsi
# currying <- Haskell Curry 

def pangkat(angka,n):
  hasil = angka ** n 
  return hasil
  
data_hasil = pangkat(5,3)
print(f'hasil fungsi biasa = {data_hasil}')

# dengan currying menjadi
def pangkat(n):
  return lambda angka : angka ** n 

pangkat_2 = pangkat(2)
print(f'hasil fungsi currying = {pangkat_2(2)}')
pangkat_4 = pangkat(4)
print(f'pangkat 4 = {pangkat_4(2)}')
print(f'pangkat bebas = {pangkat(3)(2)}')






