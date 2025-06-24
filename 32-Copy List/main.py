# Teknik menduplikat list

a = ['agus','bambang','bagas','andi']
print(f'a = {a}')

b = a # pass by reference
print(f'b = {b}')

# kita akan merubah member dari a
# ini akan merubah kedua list
a[2] = 'aron'
b.sort()
print(f'a = {a}')
print(f'b = {b}')

# menduplikat list dengan menggunakan copy

c = a.copy() # full duplikat / data baru
c[0] = 'bargon'
print(f'c = {c}')
print(f'a = {a}')






































