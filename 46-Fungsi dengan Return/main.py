# Fungsi dengan Return 

# template fungsi denga kembalian
# def nama_fungsi(argument):
#     badan fungsi 
#     Return output

# fungsi kuadrat
def kuadrat(input_angka):
  output_kuadrat = input_angka**2
  return output_kuadrat
  
print(kuadrat(5))
z = 20 + kuadrat(5) 
print(z)

# fungsi tambah
def fungsi_tambah(angka_1,angka_2):
  return angka_1 + angka_2
a = 5
b = 10
hasil = fungsi_tambah(a,b)
print(hasil)

# fungsi dengan return banyak
def operasi_matematika(angka_1,angka_2):
  tambah = angka_1 + angka_2
  kurang = angka_1 - angka_2
  kali = angka_1 * angka_2
  bagi = angka_1 / angka_2
  return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(2,4)
print(f'Hasil tambah = {k}')
print(f'Hasil kurang = {l}')
print(f'Hasil kali = {m}')
print(f'Hasil bagi = {n}')



