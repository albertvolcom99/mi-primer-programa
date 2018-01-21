"""
Dada una lista de strings, devolver una lista con el largo de cada string
"""

lista_strings = ["hola", "adios", "perro", "gato", "supercalifragillisticoespialidoso"]

lista_resultado = []

for i in lista_strings:
    lista_resultado.append(len(i))

print(lista_resultado)