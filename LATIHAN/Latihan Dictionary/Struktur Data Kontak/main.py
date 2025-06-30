print(10*'-'+'STRUKTUR DATA KONTAK'+10*'-')

# tahap 1: struktur data kontak
kontak = {
  'andi': {
    'nomor':'0853454334',
    'email':'andi123@gmail.com'
  },
  'budi': {
    'nomor':'08324234444',
    'email':'budi999@gmail.com'
  }
}

# tahap 2: menu utama
def tampilkan_menu():
  print('\n === Buku Kontak ===')
  print('1. Tampilkan semua kontak')
  print('2. Cari kontak')
  print('3. Tambah kontak')
  print('4. Hapus kontak')
  print('5. Update kontak')
  print('6. Keluar')

# tahap 3: fungsi-fungsi dasar
# lihat semua kontak
def tampilkan_kontak(kontak):
  if not kontak:
    print('Belum ada data kontak')
  else:
    for nama, data in kontak.items():
      print(f'- {nama.title()}: {data['nomor']} | {data['email']}')

# cari kontak 
def cari_kontak(kontak):
  nama = input('Nama yang dicari: ').lower()
  if nama in kontak:
    print(f'{nama.title()} - Nomor: {kontak[nama]['nomor']}, Email: {kontak[nama]['email']}')
  else:
    print('Kontak tidak ditemukan')

# tambah kontak 
def tambah_kontak(kontak):
  nama = input('Nama: ').lower()
  if nama in kontak:
    print('Kontak sudah ada.')
    return
  nomor = input('Nomor HP: ')
  email = input('Email: ')
  kontak[nama] = {'nomor' :nomor, 'email':email}
  print('Kontak berhasil ditambahkan.')
  
# hapus kontak 
def hapus_kontak(kontak):
  nama = input('Nama yang ingin dihapus: ').lower()
  if nama in kontak:
    del kontak[nama]
    print('Kontak dihapus')
  else:
    print('Kontak tidak ditemukan.')

# update kontak
def update_kontak(kontak):
  nama = input('Nama yang ingin diupdate: ').lower()
  if nama in kontak:
    nomor = input('Nomor baru: ')
    email = input('Email baru: ')
    kontak[nama] = {'nomor':nomor, 'email':email}
    print('Kontak berhasil diupdate')
  else:
    print('Kontak tidak ditemukan')

# kontak = {}

while True:
  tampilkan_menu()
  pilihan = input('Pilih menu: ')
  
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
    print('Terima kasih. Program selesai.')
    break
  else:
    print('Pilihan tidak valid.')






















