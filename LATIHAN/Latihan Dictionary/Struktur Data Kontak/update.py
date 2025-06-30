# STRUKTUR DATA KONTAK 2

import os 

def clear_screen() :
  os.system('cls' if os.name == 'nt' else 'clear')

# menu utama
def tampilkan_menu():
  clear_screen()
  print(100*'-')
  print(f'{'STRUKTUR DATA KONTAK':^100}')
  print(100*'-')
  print('\n1. Tampilkan semua kontak')
  print('2. Cari kontak')
  print('3. Tambah kontak')
  print('4. Hapus kontak')
  print('5. Update kontak')
  print('0. Keluar')
  
# lihat semua kontak 
def tampilkan_kontak(kontak):
  clear_screen()
  print(100*'-')
  print(f'{'DAFTAR KONTAK':^100}')
  print(100*'-'+'\n')
  if not kontak:
    print(f'{'BELUM ADA KONTAK':^100}')
  else:
    print(100*'-')
    print(f'{'NO':^5}| {'Nama':<35}| {'Nomor':<20}| {'Email':<40}')
    print(100*'-')
    for no,data in enumerate(kontak):
      NAMA = data
      NOMOR = kontak[NAMA]['nomor']
      EMAIL = kontak[NAMA]['email']
      print(f'{no+1:^5}| {NAMA.title():<35}| {NOMOR:<20}| {EMAIL:<40}')
    print(100*'-'+'\n')
  input('Lanjut ke menu...')
  
# cari kontak
def cari_kontak(kontak):
  nama = input('\nNama yang dicari: ').lower()
  if nama in kontak:
    clear_screen()
    print(100*'-')
    print(f'{'Nama':<35}| {'Nomor':<20}| {'Email':<40}')
    print(100*'-')
    print(f'{nama.title():<35}| {kontak[nama]['nomor']:<20}| {kontak[nama]['email']:<40}')
    print(100*'-'+'\n')
    input('Lanut ke menu...')
  else:
    input('⚠️  Kontak tidak ditemukan!')

# tambah kontak 
def tambah_kontak(kontak):
  print('\n'+30*'-'+'TAMBAH KONTAK'+30*'-')
  nama = input('\nNama\t: ').lower()
  if nama in kontak:
    input('Kontak sudah ada!!!')
    return
  
  while True:
    try:
      nomor = int(input('Nomor\t: '))
      break
    except ValueError:
      input('\n⚠️  Input harus angka!')
      
  email = input('Email\t: ')
  kontak[nama] = {'nomor':nomor, 'email':email}
  input('\nKontak berhasil ditambahkan...')

# hapus kontak 
def hapus_kontak(kontak):
  print('\n'+30*'-'+'HAPUS KONTAK'+30*'-')
  nama = input('\nNama kontak yang ingin dihapus: ')
  if nama in kontak:
    del kontak[nama]
    input('\nKontak berhasil dihapus...')
  else:
    input('\nKontak tidak ditemukan...')

# update kontak
def update_kontak(kontak):
  print('\n'+30*'-'+'UPDATE KONTAK'+30*'-')
  nama = input('Nama yang ingin diupdate: ')
  if nama in kontak:
    while True:
      try:
        nomor = int(input('Nomor baru\t: '))
        break
      except ValueError:
        input('\n⚠️  Input harus angka!')
        
    email = input('Email baru\t: ')
    kontak[nama] = {'nomor':nomor, 'email':email}
    input('\nKontak berhasil diupdate...')
  else:
    input('\nKontak tidak ditemukan...')

# struktur data kontak 
kontak = {
  'andi': {
    'nomor': '08432432',
    'email':'andi123@gmail.com'
  },
  'budi': {
    'nomor': '08324234444',
    'email':'budi999@gmail.com'
  }
}

while True:
  tampilkan_menu()
  pilihan = input('\nPilih menu: ')
  
  if pilihan == '1':
    tampilkan_kontak(kontak)
  elif pilihan == '2':
    cari_kontak(kontak)
  elif pilihan == '3':
    tambah_kontak(kontak)
  elif pilihan == '4':
    hapus_kontak(kontak)
  elif pilihan == '5':
    update_kontak(kontak)
  elif pilihan == '0':
    print(f'{'TERIMA KASIH. PROGRAM SELESAI':^100}')
    break
  else:
     input('\n⚠️  Pilihan tidak valid...')
  
  
  
  
  
  
  
  
  