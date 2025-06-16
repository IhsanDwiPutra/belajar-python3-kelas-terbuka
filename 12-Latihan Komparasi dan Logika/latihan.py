# latihan komparasi dan latihan
# 1. ----------0+++++++++5---------8++++++11------------
# 2. ++++++++++0---------5+++++++++8------11++++++++++++

input_user = int(input('----------0+++++++++5---------8++++++11------------\n: '))

# 1. ----------0+++++++++5---------8++++++11------------
is_correct = ((input_user > 0 and input_user < 5) or (input_user > 8 and
input_user < 11))
print('Hasilnya:', is_correct)

# 2. ++++++++++0---------5+++++++++8------11++++++++++++
input_user = int(input('++++++++++0---------5+++++++++8------11++++++++++++\n '))
is_correct2 = ((input_user < 0 or input_user > 5) and (input_user < 8 or
input_user > 11))
print('Hasilnya:', is_correct2)