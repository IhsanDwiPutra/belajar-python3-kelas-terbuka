# Deep Copy Nested List

data_0 = [1,2]
data_1 = [3,4]
data_2 = [5,6]

data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy()

print(f'data 2D = {data_2D}')
print(f'data 2D Copy = {data_2D_copy}')

# address semuanya
print(f'address asli = {hex(id(data_2D))}')
print(f'address copy = {hex(id(data_2D_copy))}')

print('address dari member ke-1')
print(f'address dari member      = {hex(id(data_2D[0]))}')
print(f'address dari member copy = {hex(id(data_2D_copy[0]))}')

data_2D[0][1] = 10
print(f'data = {data_2D}')
print(f'data copy = {data_2D_copy}')

data_2D.append(data_2)
print(f'data = {data_2D}')
print(f'data copy = {data_2D_copy}')

# kita gunakan deepcopy
from copy import deepcopy

data_2D_deepcopy = deepcopy(data_2D)
print(f'data asli = {data_2D}')
print(f'data deepcopy = {data_2D_deepcopy}')

print(f'address data member ke-1 = {hex(id(data_2D[0]))}')
print(f'address data deep member ke-1 = {hex(id(data_2D_deepcopy[0]))}')


# mengambil data dari nested list

data = data_2D[1][0]
# print(f'data = {data}')



























