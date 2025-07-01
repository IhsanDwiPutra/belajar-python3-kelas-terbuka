# Latihan Fungsi

import os 

# program menghitung luas dan keliling persegi panjang

# membuat haeder program
# os.system('clear')
# print(f'{'PROGRAM MENGHITUNG LUAS':^50}')
# print(f'{"DAN KELILING PERSEGI PANJANG":^50}')
# print(f'{'-'*50}')

# # mengambil input user
# LEBAR = int(input('Masukkan nilai lebar: '))
# PANJANG = int(input('Masukkan nilai panjang: '))

# # program menghitung luas 
# LUAS =  PANJANG*LEBAR 
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasilnya
# print(f'hasil perhitungan luas = {LUAS}')
# print(f'hasil perhitungan keliling = {KELILING}') 

def header():
  # fungsi header
  os.system('clear')
  print(f'{'PROGRAM MENGHITUNG LUAS':^50}')
  print(f'{"DAN KELILING PERSEGI PANJANG":^50}')
  print(f'{'-'*50}')
  
def input_user():
  # mengambil input user 
  lebar = int(input('Masukan nilai lebar: '))
  panjang = int(input('Masukan nilai panjang: '))
  
  return lebar,panjang

def hitung_luas(lebar,panjang):
  return lebar * panjang
  
def hitung_keliling(lebar,panjang):
  return 2*(lebar+panjang)
  
def tampilkan_hasil(luas,keliling):
  print(f'Hasil perhitungan luas = {luas}')
  print(f'Hasil perhitungan keliling = {keliling}')

while True:
  header()
  
  LEBAR,PANJANG = input_user()
  
  LUAS = hitung_luas(LEBAR,PANJANG)
  KELILING = hitung_keliling(LEBAR,PANJANG)
  
  tampilkan_hasil(LUAS,KELILING)
  
  isContinue = input('Lanjut? (y/n): ')
  if isContinue == 'n':
    break 
  
print('Program Selesai. Terima Kasih')

















