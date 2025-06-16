# format string

# contoh generic
# string
nama = 'agus'
format_str = f'hello {nama}'
print(format_str)

# boolean
boolean = False
format_str = f'boolean = {boolean}'
print(format_str)

# angka
angka = 32424
format_str = f'angka = {angka}'
print(format_str)

# bilangan bulat
angka = 43254354
format_str = f'bilangan bulat = {angka:d}'
print(format_str)

# bilangan ribuan
angka = 10000000
format_str = f'ribuan = {angka:,}'
print(format_str)

# bilangan desimal
angka = 432432.43
format_str = f'desimal = {angka:.10f}'
print(format_str)

# menampilkan leading zero
angka = 432432.43343
format_str = f'desimal = {angka:020.10f}'
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.343232
format_minus = f'minus = {angka_minus}'
format_plus = f'plus = {angka_plus:+.1f}'

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.023
format_persen = f'persen = {persentase:.0%}'
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 5000
jumlah = 10
format_str = f'harga total = Rp{harga*jumlah:,}'
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 35343
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hex = {hex(angka)}'

print(format_binary)
print(format_octal)
print(format_hex)




































