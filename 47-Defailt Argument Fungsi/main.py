# Default Argument

# def fungsi(argument = nilai defaultnya):
def sapa(nama = 'ganteng'):
  print(f'Hai {nama} apa kabar') 
  
sapa()
sapa('Bagas')
  
def sapa_dia(pesan,nama = 'kamu'):
  print(f'Hi {nama}, {pesan}')
  
sapa_dia('Apa kabar')
  
def hitung_pangkat(angka,pangkat):
  hasil = angka**pangkat
  return hasil
  
hasil = hitung_pangkat(pangkat = 2,angka = 5) 
print(hasil)
  
  
  
  
  
  
  
  
  
  
  
  
  