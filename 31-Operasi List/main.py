# Operasi List

data_angka = [3,6,87,3,7,4,6,2,7,9,5]
print(f'data angka = {data_angka}')

# count data
jumlah_data_6 = data_angka.count(6)
print(f'jumlah data 6 = {jumlah_data_6}')

# ambil posisi data (index)
data = ['agus','bagas','andi']
print(f'data = {data}')

index_andi = data.index('andi')
print(f'index si andi = {index_andi}')

# mengurutkan list
print(f'data angka sebelum sort = {data_angka}')
data_angka.sort()
data.sort()
print(f'data angka setelah di sort = {data_angka}')
print(f'data string setelah di sort = {data}')

# balik listnya
data_angka.reverse()
data.reverse()
print(f'data angka setelah di reverse = {data_angka}')
print(f'data string setelah di reverse = {data}')



































