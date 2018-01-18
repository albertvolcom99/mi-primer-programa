"""
Devuelve las vocales dentro de una string introducida por el usuario
"""

vocales = "aeiou"

frase = input("Escribe una frase: ")
lista_vocales = []

for i in frase:
    if i in vocales:
        lista_vocales.append(i)

print("Has usado estas vocales: {}".format(lista_vocales))
