import random
import string 

def random_string(panjang:int)->int:
   hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
   return hasil_string