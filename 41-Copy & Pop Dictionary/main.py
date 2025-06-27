# copy dictionary

teman_teman = {
  'gus':'agus markucus',
  'dong':'markondong',
  'bang':'bambang marbambang',
  'ni':'marni kumarni'
}

friend = teman_teman.copy()
print(f'teman-teman = {teman_teman}')
print(f'friends = {friend}')

teman_teman['gus'] = 'margus sibagus'
print(f'teman-teman = {teman_teman}')
print(f'friends = {friend}')

# pop dictionary
data_agus = friend.pop('gus')
print(f'data agus = {data_agus}')
print(f'friends = {friend}')

# popitem dictionary (yang terakhir saaj)
data_terakhir = friend.popitem()
print(f'data terakhir = {data_terakhir}')
print(f'friends = {friend}')





