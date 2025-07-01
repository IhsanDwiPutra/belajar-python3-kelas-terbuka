# Args pada fungsi

def sapa(*data):
  nama = data[0]
  tinggi = data[1]
  berat = data[2]
  print(f'{nama} punya tinggi {tinggi} dan berat {berat} kg')
  
sapa('agus',165,4) 

# studi kasus
def tambah(*data):
  # data tipenya adalah tuple, dia bisa diiterasi
  output = 0
  for i in data:
    output += i 
  
  return output
  
hasil = tambah(3,6,7)
print(hasil)

















