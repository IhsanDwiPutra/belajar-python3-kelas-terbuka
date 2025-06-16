# latihan komparasi dan logika
# membuat gabungan area rentang dari angka
# +++++++++++3-----------10++++++++++++++

input_user = int(input("Masukkan angka kurang dari 3 dan lebih dari 10: "))

# ++++++++3
# memeriksa angka kurang dari 3
is_kurang_dari = (input_user < 3)
print('Kurang dari 3 =', is_kurang_dari)

# --------10+++++++++
is_lebih_dari = (input_user > 10)
print('Lebih dari 10 =', is_lebih_dari)

# +++++++3-----------10+++++++++++
is_correct = is_kurang_dari or is_lebih_dari
print('Angka yang anda masukan: ', is_correct)

print('---------------------------')
# -----------3+++++++++++++10------------
# kasus irisan
input_user = int(input('Masukan angka lebih dari 3 dan kurang dari 10: '))

# --------3+++++++++
is_lebih_dari = (input_user > 3)
print('Lebih dari 3 = ', is_lebih_dari)

# +++++++++10------------
is_kurang_dari = (input_user < 10)
print('Kurang dari 10 =', is_kurang_dari)

# -----------3+++++++++10------------
is_correct = is_lebih_dari and is_kurang_dari
print('Angka yang anda masukan: ',is_correct)



































