import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  
def input_integer(message):
  while True:
    try:
      number = int(input(message))
      return number
    except ValueError:
      print('X Error: Input harus angka bulat')
      input()
      clear_screen()
      print("=== PROGRAM KONVERSI SUHU ===")

def input_float(message):
  while True:
    try:
      nilaiFloat = float(input(message))
      return nilaiFloat
    except ValueError:
      print('X Error: Input harus angka atau desimal')

is_lanjut = True
while is_lanjut:
  clear_screen()
  print("=== PROGRAM KONVERSI SUHU ===")
  input_user = input_integer("1. Celcius\n2. Reamur\n3. Fahrenheit\n4. Kelvin\n5. Keluar\nPilihan: ")
  if input_user == 1:
    clear_screen()
    print("- Konversi Suhu Celcius")
    celcius = input_float('\nMasukkan suhu dalam celcius: ')
    print('-' * 50)
    print('Suhu adalah', celcius,'celcius di konversi ke --->')
    
    reamur = (4/5) * celcius
    print('Reamur     :', reamur,'reamur')
    
    fahrenheit = (9/5) * celcius + 32
    print('Fahrenheit :', fahrenheit,'fahrenheit')
    
    kelvin = celcius + 273
    print('Kelvin     :',kelvin,'kelvin')
    
    input("\n\nTekan enter untuk lanjut\n")
  elif input_user == 2:
    clear_screen()
    print('- Konversi Suhu Reamur')
    reamur = input_float("\nMasukkan suhu dalam reamur: ")
    print('-' * 50)
    print('Suhu adalah', reamur,'reamur di konversi ke --->')
    
    celcius = (5/4) * reamur
    print('Celcius    :',celcius,'celcius')
     
    fahrenheit = (9/4) * reamur + 32
    print('Fahrenheit :',fahrenheit,'fahrenheit')
    
    kelvin = (5/4) * reamur + 273
    print('Kelvin     :',kelvin,'kelvin')
    
    input("\n\nTekan enter untuk lanjut\n")
  elif input_user == 3:
    clear_screen()
    print('- Konversi Suhu Fahrenheit')
    fahrenheit = input_float("\nMasukkan suhu dalam fahrenheit: ")
    print('-' * 50)
    print('Suhu adalah', fahrenheit,'fahrenheit di konversi ke --->')
    
    celcius = 5 / 9 * (fahrenheit-32)
    print('Celcius    :',celcius,'celcius')
    
    reamur = 4 / 9 * (fahrenheit-32)
    print('Reamur     :',reamur,'reamur')
    
    kelvin = 5 / 9 * (fahrenheit-32) + 273
    print('Kelvin     :',kelvin,'kelvin')
    
    input("\n\nTekan enter untuk lanjut\n")
  elif input_user == 4:
    clear_screen()
    print('- Konversi Suhu Kelvin')
    kelvin = input_float("\nMasukkan suhu dalam kelvin: ")
    print('-' * 50)
    print('Suhu adalah', kelvin,'kelvin di konversi ke --->')
    
    celcius = kelvin - 273
    print('Celcius    :',celcius,'celcius')
    
    reamur = 4 / 5 * (kelvin - 273)
    print('Reamur     :',reamur,'reamur')
    1
    fahrenheit = 9 / 5 * (kelvin - 273) + 32
    print('Fahrenheit :',fahrenheit,'fahrenheit')
    
    input("\n\nTekan enter untuk lanjut\n")
  elif input_user == 5:
    print("\nTerima Kasih Sudah Mampir")
    input()
    break;
  else:
    print('Pilihan tidak ditemukan!!!')
    input()























