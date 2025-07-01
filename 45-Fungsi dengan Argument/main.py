# Fungsi dengan Argument (input)
def sapa(nama):
  print('Hai ' + nama + " selamat datang")
  
sapa('Agus')

def tambah(angka_1,angka_2):
  hasil = angka_1 + angka_2
  print(f'{angka_1} + {angka_2} = {hasil}')

tambah(5,9)

def say_hi(anggota):
  anggotaa = anggota.copy()
  for nama in anggotaa:
    print(f'Hai {nama} yang ganteng')
    
anggota_band = ['Agus','Andi','Bagas']

say_hi(anggota_band)








