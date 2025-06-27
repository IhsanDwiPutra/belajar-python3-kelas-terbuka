# key, nama penulis, judul, penerbit, tahun rilis

import datetime
import string
import random
import os

def clear_screen() :
  os.system('cls' if os.name == 'nt' else 'clear')

valid = {
  True:'Ya',
  False:'Tidak'
}

template_buku = {
  'nama':'nama',
  'judul':'judul',
  'penerbit':'penerbit',
  'tahun_rilis':datetime.datetime(1111,1,1),
  'valid':True
}

data_buku = {}

while True:
  clear_screen()
  print(f"{'SELAMAT DATANG DI':^30}")
  print(f"{'DATA BUKU':^30}")
  print(35*'-')
  
  buku = dict.fromkeys(template_buku)
  
  
  buku['nama'] = input('Nama Penulis\t\t: ')
  buku['judul'] = input('Judul Buku\t\t: ')
  buku['penerbit'] = input('Penerbit\t\t: ')
  
  # Try Except
  while True:
    try:
      TAHUN_RILIS = int(input('Tahun rilis (YYYY)\t: '))
      BULAN_RILIS = int(input('Bulan rilis (1-12)\t: '))
      HARI_RILIS = int(input('Tangal rilis (1-31)\t: '))
      try:
        buku['tahun_rilis'] = datetime.datetime(TAHUN_RILIS,BULAN_RILIS,HARI_RILIS)
        break
      except ValueError:
        print('\n⚠️  Ada yang salah nih!!!')
    except ValueError:
      print('\n⚠️  Masukkan harus berupa angka!!!')
    
  buku['valid'] = random.choice([True,False])
  
  KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
  
  isTambah = input('\nTambahkan Buku? (y/n): ')
  if isTambah == 'n':
    if len(data_buku) == 0:
      continue
    
    print('\n'+100*'-')
    print(f"|{'NO':^2}| {'KEY':^4}| {'Nama Penulis':^25}| {'Judul Buku':^25}| {'Penerbit':^15}| {'Tahun':^10}| {'Valid':<7}")
    print(100*'-')
  
    for no,buku in enumerate(data_buku):
      NO = no+1
      KEY = buku 
      NAMA = data_buku[KEY]['nama']
      JUDUL = data_buku[KEY]['judul']
      PENERBIT = data_buku[KEY]['penerbit']
      TAHUN_RILIS_BUKU = data_buku[KEY]['tahun_rilis'].strftime('%x')
      VALID = valid[data_buku[KEY]['valid']]
      
      print(f'|{NO:<2}| {KEY:<4}| {NAMA:<25}| {JUDUL:<25}| {PENERBIT:<15}| {TAHUN_RILIS_BUKU:^10}| {VALID:<7}')

    print(100*'-'+'\n')
    input('Tekan "Enter" untuk melanjutkan...')
    continue
  
  data_buku.update({KEY:buku})
  
  print('\n'+100*'-')
  print(f"|{'NO':^2}| {'KEY':^4}| {'Nama Penulis':^25}| {'Judul Buku':^25}| {'Penerbit':^15}| {'Tahun':^10}| {'Valid':<7}")
  print(100*'-')
  
  for no,buku in enumerate(data_buku):
    NO = no+1
    KEY = buku 
    NAMA = data_buku[KEY]['nama']
    JUDUL = data_buku[KEY]['judul']
    PENERBIT = data_buku[KEY]['penerbit']
    TAHUN_RILIS_BUKU = data_buku[KEY]['tahun_rilis'].strftime('%x')
    VALID = valid[data_buku[KEY]['valid']]
    
    print(f'|{NO:<2}| {KEY:<4}| {NAMA:<25}| {JUDUL:<25}| {PENERBIT:<15}| {TAHUN_RILIS_BUKU:^10}| {VALID:<7}')
    
  print(100*'-'+'\n')
  isLanjut = input('Tambah Lagi? (y/n): ')
  if isLanjut == 'n':
    break
    

print(100*'-')
print('TERIMA KASIH TELAH BERKUNJUNG')