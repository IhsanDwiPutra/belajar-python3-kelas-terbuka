# __main__ adalah top level code environment
# __name__ == "__main__" akan terjadi jika ada di program utama

## __name__ pada file program utama
print(f"nilai __name__ pada main_app.py = '{__name__}'")

## __name__ pada file program external
import fungsi

import package

#3 contoh penggunaan __main__
# deklarasi
def fungsi_tambah(a:int,b:int)->int:
  return a + b 

# fungsi utama
if __name__ == "__main__":
  angka_1 = 5
  angka_2 = 12
  hasil = fungsi_tambah(angka_1,angka_2)
  print(f"hasil tambah = {hasil}")
  
## import package
import package
















