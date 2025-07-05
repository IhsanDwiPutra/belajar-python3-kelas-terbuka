# Package 
# import time 

# t_start = time.time()
import sains.matematika
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(3,4,56,34,3,4,3)
print(f"hasil tambah dari package adalah = {hasil_tambah}") 


hasil_gaya = fisika.gaya(2,6)
print(f"hasil gaya = {hasil_gaya}")

gaya = force(30,6)
print(f"hasil gaya = {gaya}")


# t_end = time.time
# print(f"waktu eksekusi adalah = {type(t_end - t_start)}")






