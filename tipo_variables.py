"""
Tipos de datos dentro de una lista
"""

lista = [1, "hola", 2.3, [], True]
tipos = []

for i in lista:
    tipos.append(type(i))

print (tipos)