"""
Multiplicar y solo mostrar los pares
"""

numero = int(input("Número a multiplicar: "))

for i in range(1,11):
    if numero*i%2==0:
        print("{} X {} = {}".format(numero, i, numero*i))

