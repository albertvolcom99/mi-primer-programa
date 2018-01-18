"""
Multiplicar del 5 al 15
"""

numero = int(input("Número a multiplicar: "))

for i in range(5,16):
    print("{} X {} = {}".format(numero, i, numero*i))

