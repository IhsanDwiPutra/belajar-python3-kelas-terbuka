# List Exercises
# program list buku

list_buku = []
while True:
  print('\nMasukan Data Buku!!!')
  judul = input('Judul buku\t: ')
  penulis = input('Nama penulis\t: ')
  
  buku_baru = [judul,penulis]
  list_buku.append(buku_baru)
  
  print('\n'+50*'-')
  print(f'NO | Judul               | Nama Penulis   ')
  print(50*'-')
  for no,data in enumerate(list_buku):
    print(f'{no+1:<3}| {data[0]:<20}| {data[1]:<15}')
  
  print(50*'-'+'\n')
  
  isLanjut = input('Tambahkan buku? (y/n) : ')
  if isLanjut != 'y':
    break
  
print('Sekian Terima Gaji')


























