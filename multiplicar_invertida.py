"""
Multiplicar del 10 al 1
"""

numero = int(input("Número a multiplicar: "))

for i in range(10,0, -1):
    print("{} X {} = {}".format(numero, i, numero*i))

