"""
Cuenta el numero de mayusculas que tiene una frase
"""

frase = input("Escribe una frase: ")
suma = 0

for i in frase:
    if i == i.upper():
        suma += 1

print("El número de mayúsculas es: {}".format(suma))