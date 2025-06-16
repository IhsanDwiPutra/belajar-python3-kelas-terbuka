# operasi dan manipulasi string part 2

# merubah case dari string
# merubah semua ke upper case
salam = 'bro!'
print('normal = ' + salam + ' , upper case = ' + salam.upper())

# merubah semua ke lower case
perhatian = 'WARNING DILARANG MASUK!!!'
print('normal = ' + perhatian + ' , lower case = ' + perhatian.lower())

# pengecekan dengna isX method
# contoh pengecekan lower case
salam = 'halo'
apakah_lower = salam.islower() # hasilnya boolean
print(salam + ' is lower = ' + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + ' is upper = ' + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi,tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

# isjudul()
judul = 'A Beatiful World'
is_judul = judul.istitle()
print(judul + ' is judul = ' + str(is_judul))

# penggabungan komponen join() split()
status = ['aku','sangat','lapar']
print('-'.join(status))

# alokasi karakter rjust(), ljust(), center()
kanan = 'kanan'.rjust(10)
print("'"+kanan+"'")

kiri = 'kiri'.ljust(10)
print("'"+kiri+"'")

tengah = 'tengah'.center(10,'-')
print("'"+tengah+"'")

# kebalikannya --> strip()
tengah = tengah.strip('-') # menghilangkan tanda '-'
print("'"+tengah+"'")































