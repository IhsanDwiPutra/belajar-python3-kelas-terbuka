# module matematika dengan import 

from matematika import tambah as add
from matematika import kali as kl 
from matematika import pangkat as pkt
# from matematika import *

import matematika as math # <-- bisa dilakukan

hasil_tambah = add(5,4,5,3,1)
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = math.kali(3,5,3,5,3) 
print(f"hasil kali = {hasil_kali}")

pangkat_3 = pkt(3)
print(f"hasil pangkat 3 dari 3 = {pangkat_3(3)}")





