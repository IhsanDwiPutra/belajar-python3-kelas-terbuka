# Continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi
i = 0
while i < 5:
  i+=1
  if i == 2:
    pass # ini tidak akan dieksekusi
  print('hai bang ke-'+str(i)) # aksi 1
  
  if i == 4:
    print('woi bang')
    continue # akan membuat loop meloncat ke step selanjutnya
  
  print('mantap') # aksi 2
  

























