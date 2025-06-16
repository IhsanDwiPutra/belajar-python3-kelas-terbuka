# width and Multiline

# data
data_nama = 'Agus Marcup'
data_umur = 23
data_tinggi = 168.5
data_nomor_sepatu = 43

# string standard
data_string = f'nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}'
print(5*'='+'Data String'+5*'=')
print(data_string)

# string multiline (dengan menggunakan enter, newline \n)
data_string = f'nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}'
print('\n'+5*'='+'Data String'+5*'=')
print(data_string)

# string multiline (kutip triplets)
print('\n'+5*'='+'Data String'+5*'=')
data_string = (f'''
nama    = {data_nama}
umur    = {data_umur}
tinggi  = {data_tinggi}
sepatu  = {data_nomor_sepatu}
''')
print(data_string)

# mengatur lebar
print('\n'+5*'='+'Data String'+5*'=')
data_nama = 'agus'
data_string = (f'''
nama    = {data_nama:>5}
umur    = "{data_umur:^10}"
tinggi  = {data_tinggi:>6}
sepatu  = {data_nomor_sepatu:>4}
''')
print(data_string)

























