# Nested List / List Bersarang

data_1 = [1,2]
data_2 = [3,4]

data_list_biasa = [1,2,3,4]
print(f'list biasa - {data_list_biasa}')

list_2D = [data_1,data_2,data_list_biasa,2,5,'bagas']
print(f'list 2D = {list_2D}')

# contoh penggunaan
peserta_0 = ['bagas',12,'laki-laki']
peserta_1 = ['marni',23,'wanita']

list_peserta = [peserta_0,peserta_1]
print(f'peserta = {list_peserta}')

for data in list_peserta:
  print(f'------------------\nNama   : {data[0]}\nUmur   : {data[1]}\nGender : {data[2]}')

# dengan reference

















