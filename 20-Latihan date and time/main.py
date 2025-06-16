# date and time

import datetime as dt

# Dictionary untuk terjemahan hari
nama_hari = {
  'Monday': 'Senin',
  'Tuesday': 'Selasa',
  'Wednesday': 'Rabu',
  'Thursday': 'Kamis',
  'Friday': 'Jum\'at',
  'Saturday': 'Sabtu',
  'Sunday': 'Minggu'
}

# Tanggal lahir
print('Silahkan masukan tanggal, \nbulan dan tahun lahir anda')
tanggal = int(input('Tanggal : '))
bulan = int(input('Bulan \t: '))
tahun = int(input('Tahun \t: '))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f'Tahun lahir anda adalah : {tanggal_lahir}')
print(f'Hari nya adalah : {nama_hari[tanggal_lahir.strftime('%A')]}')

# Hari ini
hari_ini = dt.date.today()
print(f'Hari ini tanggal : {hari_ini}')

# Hitung umur
umur_hari = hari_ini - tanggal_lahir
umur_hari_total = umur_hari.days

umur_tahun = umur_hari_total // 365
sisa_hari_setelah_tahun = umur_hari_total % 365

umur_bulan = sisa_hari_setelah_tahun // 30
sisa_hari = sisa_hari_setelah_tahun % 30

# Output
print(f'Umur anda adalah : {umur_tahun} tahun, {umur_bulan} bulan, {sisa_hari} hari')

















































