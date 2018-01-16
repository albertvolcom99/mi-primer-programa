"""
Contar vocales y consonantes de una frase
"""

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
