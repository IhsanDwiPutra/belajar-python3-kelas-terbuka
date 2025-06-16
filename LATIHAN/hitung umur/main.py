from datetime import datetime

# 1. Ambil tahun saat ini
tahun_sekarang = datetime.now().year

# 2. Input dari pengguna
nama = input('Masukkan nama Anda: ')

while True:
  try:
    tahun_lahir = int(input('Masukkan tahun lahir Anda (Contoh: 2000): '))
    break
  except ValueError:
    print('X Masukkan harus berupa angka tahun lahir')

# 3, Hitung umur
umur = tahun_sekarang - tahun_lahir

# 4. Tampilkan hasil
print('='*20)
print(f'Hai {nama}, umur Anda sekarang adalah {umur}')


























