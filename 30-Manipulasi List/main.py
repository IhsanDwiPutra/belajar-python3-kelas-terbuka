# Manipulasi list

## Operasi

# index   0(-3)       1(-2        2(-1)
data = ['agus','bambang','bagas']

# mengambil data dari list ini
data_0 = data[0]
data_1 = data[1]
data_2 = data[2]
print(f'data pertama (index ke-0) = {data_0}')

data_terakhir = data[-1]
print(f'data terakhir adalah = {data_terakhir}')

data_agus = data[-3]
print(f'data agus = {data_agus}')

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f'panjang data ini {data} adalah = {panjang_data}')

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f'data sebelum ditambah = {data}')
data.insert(0,'asep')  # data.insert(posisi,item)
print(f'data setelah ditambah = {data}')

# menambah di akhir list
data.append('sugeng')
print(f'data setelah ditambah = {data}')

# menambah list dengan list
data_baru = ['ayup','marni','marko']
data.extend(data_baru)
print(f'data setelah diextend = {data}')

# merubah data
# kita ubah data ke 3 menjadi andi
data[3] = 'andi'
print(f'data setelah diubah = {data}')

# meremove data
data.remove('asep') # huruf harus sesuai jika tidak akan error
print(f'data setelah asep ditendang = {data}')

# meremove data paling belakang
data.pop()
print(f'data setelah diremove di belakang {data}')































