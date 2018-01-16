"""
Tabla de multiplicar
"""
user_number = ""

while not(user_number.isdigit()):
    user_number = input("¿Que numero quieres multiplicar?")


for i in range(1,11):
    print ("{} X {} = {}".format((user_number), (i), (int(user_number)*i)))

