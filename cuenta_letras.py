"""
Contar vocales, consonantes, espacios, puntos y comas de una frase
"""

vocales = "aeiou"
consonantes = "bcdfghjklmnñpqrstvwxyz"
total_vocales = 0
total_consonantes = 0
total_espacios = 0
total_comas = 0
total_puntos = 0

frase = input("Frase: ")

for i in frase:
    if i in vocales:
        total_vocales += 1
    elif i in consonantes:
        total_consonantes += 1
    elif i == " ":
        total_espacios += 1
    elif i == ".":
        total_puntos += 1
    elif i == ",":
        total_comas += 1

print("Total vocales: {}".format(total_vocales))
print("Total consonantes: {}".format(total_consonantes))
print("Total espacio: {}".format(total_espacios))
print("Total puntos: {}".format(total_puntos))
print("Total comas: {}".format(total_comas))