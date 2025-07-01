# Type Hints pada Fungsi

# bentuk standar fungsi yang udah dipelajari
'''
Studi kasus
def fungsi(parameter):
  print(parameter)

fungsi(1) 
fungsi(True)
'''

# penggunaan type hints 
def sepuluh_pangkat(argument:int) -> int:
  output = 10**argument
  return output
  
hasil = sepuluh_pangkat(10)
print(f'{hasil:,}')

import string 

def display(argument:string):
  print(argument)
  
display('hai bro')













