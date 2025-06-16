# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = 'Agus'
nama_tengah = 'D'
nama_akhir = 'Pra'

nama_lengkap = nama_pertama+' '+nama_tengah+' '+nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print('Panjang kata ini', nama_lengkap,'adalah',panjang)

# 3. operator untuk string
# menegecek apakah ada komponen char atau string di string

d = 'Agus'
status = d in nama_lengkap
print(d + ' ada di ' + nama_lengkap + ' = ' + str(status))

d = 'Agus'
status = d not in nama_lengkap
print(d + ' tidak  ada di ' + nama_lengkap + ' = ' + str(status))

# mengulang string
print('awok'*20)

# indexing
print('indexing ke-0: ' + nama_lengkap[0])
print('indexing ke-1: ' + nama_lengkap[1])
print('indexing ke-8 ' + nama_lengkap[8])
print('indexing ke-(-1) ' + nama_lengkap[-1])
print('indexing ke-[0:3] ' + nama_lengkap[0:4])
print('indexing ke-[7:9] ' + nama_lengkap[7:10])
print('indexing ke-[genap] ' + nama_lengkap[0:10:2])

# item paling kecil
print('paling kecil: ' + min(nama_lengkap))
# item paling besar
print('paling besar: ' + max(nama_lengkap))

# 4. operator dalam bentuk method
data = 'agus margus subagus'
jumlah = data.count('u')
print('jumlah u pada ' + data + ' = ' + str(jumlah))






































