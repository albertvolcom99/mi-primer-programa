"""
Crear un programa que cambie las vocales por su número de aparición
"""

texto = input("Escribe: ")
vocales = "aeiou"
contador = 1

for i in texto:
    if i in vocales:
        texto = texto.replace(i, str(contador), 1)
        contador += 1

print(texto)