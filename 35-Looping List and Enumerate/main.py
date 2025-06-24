# Looping List and Enumerate

# for loop
print('For Loop')
kumpulan_angka = [2,5,6,3,6,3,2]

for angka in kumpulan_angka:
  print(f'angka = {angka}')
  
peserta = ['agus','bagas','marni']
for nama in peserta:
  print(f'nama = {nama}')

# for loop dan range
print('\nFor Loop dan Range')
kumpulan_angka = [4,2,7,9,1]
panjang = len(kumpulan_angka)
for i in range(panjang):
  print(f'{i} angka = {kumpulan_angka[i]}')

# while
print('\nWhile')
kumpulan_angka = [1,4,5,3]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
  print(f'angka = {kumpulan_angka[i]}')
  i+=1

# list comprehension
print('\nList comprehension')
data = ['agus',3,5,'bagas']
[print(f'data = {i}') for i in data]

# enumerate
print('\nEnumerate')
data = ['agus',3,5,'bagas']

for index,data in enumerate(data):
  print(f'{index+1}. Data = {data}')

angka = [2,5,3,5,3]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)


































