# Multi Keys & Nesting Dictionary

import datetime

mahasiswa1 = {
  'nama':'Agus Markucus',
  'nim':'23421331',
  'sks_lulus':250, 
  'beasiswa':True,
  'lahir':datetime.datetime(1998,8,17)
}

mahasiswa2 = {
  'nama':'Bambang Marbambang',
  'nim':'43243243',
  'sks_lulus':143, 
  'beasiswa':False,
  'lahir':datetime.datetime(1993,1,12)
}

mahasiswa3 = {
  'nama':'Bagas Margas',
  'nim':'554355566',
  'sks_lulus':43, 
  'beasiswa':True,
  'lahir':datetime.datetime(1983,5,23)
}

data_mahasiswa = {
  'MAH1':mahasiswa1,
  'MAH2':mahasiswa2,
  'MAH3':mahasiswa3
}

print(f'{'KEY':<4}| {'Nama':<25}| {'SKS':<4}| {'Lahir':<10}')
print(50*'-')

for mahasiswa in data_mahasiswa:
  KEY = mahasiswa
  NAMA = data_mahasiswa[KEY]['nama']
  SKS = data_mahasiswa[KEY]['sks_lulus']
  LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')
  
  print(f'{KEY:<4}| {NAMA:<25}| {SKS:<4}| {LAHIR:<10}')












