# Latihan Perulangan membuat segitiga

sisi = 5

# 1. Menggunakan For
# dummy variable
print('1. awal for')
count = 1
for i in range(sisi):
  print('*'*count)
  count+=1
print('akhir for\n')

# 2. Menggunakan While
print('2. awal while')
count = 1
while True:
  print('*'*count)
  count+=1
  if count > sisi:
    break
  
print('akhir while')

# 3. Hanya ganjil saja
sisi = 10
print('\n3. Hanya ganjil saja')
count = 1
while True:
  if count % 2:
    # print jika ganjil
    print('*'*count)
    count+=1
  else:
  # akan kembali ke atas jika genap
    count+=1
    continue
  
  # akan break jika count melebihi sisi
  if count > sisi:
    break
  
print('akhir ganjil')

# 4. segitiga sama kaki
sisi = 10
spasi = int(sisi/2)
print('\n4. Segitiga sama kaki')
count = 1
while True:
  if count % 2:
    # print jika ganjil
    print(' '*spasi+'+'*count)
    count+=1
    spasi -=1
  else:
  # akan kembali ke atas jika genap
    count+=1
    continue
  
  # akan break jika count melebihi sisi
  if count > sisi:
    break
  
print('akhir segitia sama kaki')

# 5. Ketupat (tugas)
print('\n5. Ketupat')
tinggi = 5 # jumlah baris tengah (maksimal lebar)

# bagian atas
baris = 0
while baris < tinggi:
  spasi = tinggi - baris - 1
  while spasi > 0:
    print(' ', end='')
    spasi -= 1
  
  kolom = 0
  while kolom < 2 * baris + 1:
    print('+', end='')
    kolom += 1
    
  print()
  baris += 1
  
# bagian bawah
baris = tinggi - 2 # mulai dari satu baris di bawah puncak
while baris >= 0:
  spasi = tinggi - baris - 1
  while spasi > 0:
    print(' ', end='')
    spasi -= 1
  
  kolom = 0
  while kolom < 2 * baris + 1:
    print('+', end='')
    kolom += 1
  
  print()
  baris -= 1

print('akhir ketupat')








