"""
Dada una lista de enteros y strings, devolver dos listas,
una con todos los enteros y otra con todas las strings
"""


lista = ["hola", 3, "adios", 7, 4, "perro", "gato"]

strings = []
enteros = []

for i in lista:
    if type(i)==str:
        strings.append(i)
    else:
        enteros.append(i)

print(strings)
print(enteros)