# break

i = 0

while i < 5:
  i+=1
  print(f'Hai bro ke-{i}')
  
  if i == 3:
    print('cukup!!!')
    break
  print('whatswap')

print('akhir dari program')

input_user = int(input('hitung sampai: '))
i = 0
while True:
  print('angka ke-'+ str(i+1))
  i+=1
  if i == input_user:
    break