# Latihan Dictionary Part 1 

import datetime
import os
import string 
import random

def clear_screen() :
  os.system('cls' if os.name == 'nt' else 'clear')

# template dict mahasiswa
mahasiswa_template = {
  'nama':'nama',
  'nim':'00000000',
  'sks':0,
  'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
  
  clear_screen()
  print(f'{"SELAMAT DATANG":^25}')
  print(f"{'DATA MAHASISWA':^25}")
  print(25*'-')
  
  mahasiswa = dict.fromkeys(mahasiswa_template.keys()) # dapat Dictionary none 
  mahasiswa['nama'] = input('Nama Mahasiswa: ')
  mahasiswa['nim'] = input('NIM Mahasiswa: ')
  mahasiswa['sks'] = int(input('SKS Mahasiswa: '))
  TAHUN_LAHIR = int(input('Tahun lahir (YYYY): '))
  BULAN_LAHIR = int(input('Bulan lahir (1-12): '))
  HARI_LAHIR= int(input('Tanggal lahir (1-31): '))
  mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,HARI_LAHIR)
  
  KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(3)))
  data_mahasiswa.update({KEY:mahasiswa})
  
  print(f'{'KEY':<4}| {'Nama':<25}| {'NIM':<10}| {'SKS':<4}| {'Lahir':<10}')
  print(65*'-')
  
  for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f'{KEY:<4}| {NAMA:<25}| {NIM:<10}| {SKS:<4}| {LAHIR:<10}')
  
  isLanjut = input('Tambahkan lagi ? (y/n): ')
  if isLanjut != 'y':
    break

print('Terima Kasih Brooo')























