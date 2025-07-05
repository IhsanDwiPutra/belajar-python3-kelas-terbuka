# import 

# fungsinya adalah untuk mengambil program dari file external .py 

# 1. untuk menyambung program dari external
import program_print
import program_agus

# 2. import dengan data
import variabel
import contact

# data ada di namespace variabel
print(variabel.data)
print(contact.no)

# import dengan fungsi
import fungsi
 
fungsi.say_hi("agus")
hasil = fungsi.tambah(4,2)
print(hasil)





