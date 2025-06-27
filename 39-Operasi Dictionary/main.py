# Operasi / Operator Dictionary
data_dict = {
  'gus':'agus',
  'bam':'bambang',
  'and':'andi'
}

# panjang dictionary 
LENDICT = len(data_dict)
print(f'panjang dictionary: {LENDICT}')

# mengecek key exist atau tidak
KEY = 'gus'
CHECKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data_dict: {CHECKKEY}')

# mengakses value (read) dengan get 
print(data_dict.get('gus'))
print(data_dict.get('gas','Key tidak ditemukan')) # cek key dengan message tidak ditemukan

# mengupdate data 
data_dict['gus'] = 'bagus'
print(data_dict)
data_dict['meng'] = 'ahmeng'
print(data_dict)

data_dict.update({'gus':'agus'})
print(data_dict)
data_dict.update({'dur':'undur'}) # kalau tidak ada di add aja 
print(data_dict)

# mendelete data pada dictionary
del data_dict['dur']
print(data_dict)

































