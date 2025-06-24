# LIST

# kumpulan data numbers
data_angka = [1,2,6,3]
print(data_angka)

# kumpulan data string
data_string = ['agus','bambang','odeh']
print(data_string)

# kumpulan data booleans
data_boolean = [True,False,True,False]
print(data_boolean)

# kumpulan campuran
data_campuran = [1,'Indomie',2,'Energen','bagas',False]
print(data_campuran)

## cara alternatif membaut list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
data_list_for = [i**5 for i in range(0,10)]
print(data_list_for)

# membuat list pakai for dan if
list_for_if = [i for i in range(0,10) if i != 5]
print(list_for_if)

# mendapatkan genap
list_for_if = [i**2 for i in range(10) if i % 2 == 0]
print(list_for_if)

# mendapatkan ganjil
list_for_if = [i**2 for i in range(10) if i % 2 != 0] # menggunakan ini juga bisa i % 2
print(list_for_if)
















