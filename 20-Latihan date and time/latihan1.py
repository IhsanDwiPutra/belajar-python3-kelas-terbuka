# latihan date and time

import datetime as dt
import os

# fungsi
def clear_screen() :
  os.system('cls' if os.name == 'nt' else 'clear')

# dictionary untuk terjemahan hari
nama_hari = {
  'Monday': 'Senin',
  'Tuesday': 'Selasa',
  'Wednesday': 'Rabu',
  'Thursday': 'Kamis',
  'Friday': 'Jum\'at',
  'Saturday': 'Sabtu',
  'Sunday': 'Minggu'
}

while True:
  clear_screen()
  print(f'''{40*'='}
📅 PROGRAM HITUNG UMUR SEDERHANA 📅
{40*'='}''')
  
  # Try Except untuk Input
  while True:
    try:
      tanggal = int(input('Masukkan tanggal lahir (1-31)    : '))
      bulan = int(input('Masukkan bulan lahir (1-12)      : '))
      tahun = int(input('Masukkan tahun lahir (misal 2000): '))
      tanggal_lahir = dt.date(tahun,bulan,tanggal)
      break
    except ValueError:
      print('\n⚠️  Masukkan harus berupa angka!!!')
  
  # Tanggal lahir
  print('\n\n\n'+50*'-')
  print(f'📅 Tanggal Lahir Anda  : {tanggal_lahir}')
  hari_indonesia = nama_hari[tanggal_lahir.strftime('%A')]
  print(f'📅 Hari Lahir Anda     : {hari_indonesia}')
  
  # Hitung umur
  hari_ini = dt.date.today()
  umur_hari = hari_ini - tanggal_lahir
  umur_hari_total = umur_hari.days
  
  umur_tahun = umur_hari_total // 365
  sisa_hari_setelah_tahun = umur_hari_total % 365
  
  umur_bulan = sisa_hari_setelah_tahun // 30
  sisa_hari = sisa_hari_setelah_tahun % 30
  
  # Outoput
  print(f'🔢 Umur Anda           : {umur_tahun} tahun, {umur_bulan} bulan, {sisa_hari} hari')
  print(50*'-')
  
  
  
  ulang = input('\nIngin hitung umur lagi? (y/n): ').lower()
  if ulang != 'y':
    print('\n👏 Terima kasih sudah menggunakan program ini!')
    break








































