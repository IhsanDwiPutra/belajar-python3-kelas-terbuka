# **kwargs pada Fungsi

def fungsi(nama,tinggi,berat):
  # fungsi biasa
  print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
  
fungsi('agus',165,40)


# fungsi kwagrs
def fungsi(**kwagrs):
  nama = kwagrs['nama']
  tinggi = kwagrs['tinggi']
  berat = kwagrs['berat']
  print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
  
fungsi(nama='agus',tinggi=165,berat='540')

# studi kasus
def math(*args,**kwagrs):
  output = 0 
  if kwagrs['option'] == 'tambah':
    for angka in args:
      output +=angka
  elif kwagrs['option'] == 'kali':
    output = 1
    for angka in args:
      output *= angka
      
  return output
  
hasil = math(1,2,3,4,option='tambah')
print(f'hasil tambah = {hasil}')
hasil = math(2,2,2,option='kali')
print(f'hasil kali = {hasil}')
  









