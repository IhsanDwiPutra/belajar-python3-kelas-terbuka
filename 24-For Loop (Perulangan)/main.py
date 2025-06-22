# Perulangan (Loop)

# for kondisi:
#   aksi

# ini dengan list
print('=== Ini dengan List ====')
angka2 = [0,4,1,5,6] # ini adalah list
print(angka2)

for i in angka2:
  print(f'sekarang i ke-{i+1}')
  
print('akhir dari program 1\n')


# ini dengan range
print('=== Ini dengan Range ====')
angka2_range = range(5)
for i in angka2_range:
  print(f'Sekarang i ke-{i}')
print('akhir dari program 2\n')

angka2_range = range(1,11)
for i in angka2_range:
  print(f'Sekarang i ke-{i}')
print('akhir dari program 3\n')

# menggunakan string
data_str = 'saya sangat baik'
for huruf in data_str:
  print(huruf)
print('akhir dari program 4\n')







