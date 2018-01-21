"""
Crear un programa que encuentre el número más grande de una lista (sin usar la función max)
"""

numbers = [12, 45, 1, 7, 20, 12, 56, 87, 12]
mayor = 0

for i in numbers:
    if i>mayor:
        mayor = i

print(mayor)