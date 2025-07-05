## Global dan Local Scope

nama_global = "agus" # <- ini variable global 

# akses variabel global dalam fungsi 
def fungsi():
  print(f"Fungsi menampilkan {nama_global}")
  
fungsi()

# akses variabel global dalam loop
for i in range(0,5):
  print(f"loop {i} - {nama_global}")

# percabangan
if True:
  print(f'if menampilkan {nama_global}')


## variabel local scope 
def fungsi2():
  nama_local = "Bagas" # <- ini adalah variabel local scope 

fungsi2() 
# print(nama_local) # tidak bisa dilakuakn

## contoh 1: penggunaan akses variabel
def say_agus():
  print(f'Hello {nama}')

nama = "agus"
say_agus()

## contoh 2: merubah variabel global 
angka = 0
nama = "bagas"
def ubah_angka(nilai_baru,nama_baru = "ganteng"): 
  global angka, nama 
  angka = nilai_baru
  nama = nama_baru

print(f'Sebelum {angka,nama}')
ubah_angka(50,"andi")
print(f'Sesudah {angka,nama}')

## contoh 3: 
angka = 0 
for i in range(0,5):
  angka += i 
  angka_dummy = 50 
  
print(angka)
print(angka_dummy)

if True:
  angka = 14
  angka_dummy = 20
  
print(angka)
print(angka_dummy)









