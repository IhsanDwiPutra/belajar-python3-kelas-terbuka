# Latihan percabangan - Kalkulator Sederhana

# kalkulator sederhana
print(20*'=' + ' KALKULATOR SEDERHANA ' + 20*'=' + '\n')
angka_1 = float(input('Masukkan angka pertama: '))
operator = input('Operatornya (misal: +,-,x,/): ')
angka_2 = float(input('Masukkan angka kedua: '))

if operator == '+':
  hasil = angka_1 + angka_2
  print(f'{angka_1} + {angka_2} = {hasil}')
elif operator == '-':
  hasil = angka_1 - angka_2
  print(f'{angka_1} - {angka_2} = {hasil}')
elif operator.lower() == 'x':
  hasil = angka_1 * angka_2
  print(f'{angka_1} x {angka_2} = {hasil}')
elif operator == '/':
  hasil = angka_1 / angka_2
  print(f'{angka_1} / {angka_2} = {hasil}')
else: print('Pasti ada yang salah!!!')

print('Akhir dari program, sekian terima gaji')






































