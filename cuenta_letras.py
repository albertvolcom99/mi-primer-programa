"""
Contar vocales y consonantes de una frase
"""

"""  FORMA 1 - CON LISTAS  """

vocales = ["a", "e", "i", "o", "u"]
total_vocales = 0
total_consonantes = 0

phrase = input("Dime una frase: ")

for i in phrase:
    if i in vocales:
        total_vocales += 1
    elif i != " ":
        total_consonantes += 1

print("TOTAL DE VOCALES: {}".format(str(total_vocales)))
print("TOTAL DE CONSONANTES: {}".format(str(total_consonantes)))

""" FORMA 2 - SIN LISTAS """

vocales = "aeiou"
consonantes = "bcdfghjklmnñpqrstvwxyz"
total_vocales = 0
total_consonantes = 0

frase = input("Frase: ")

for i in frase:
    if i in vocales:
        total_vocales += 1
    if i in consonantes:
        total_consonantes += 1

print("Total vocales: {}".format(total_vocales))
print("Total consonantes: {}".format(total_consonantes))