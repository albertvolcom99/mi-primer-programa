"""
Creqa una función que muestre por pantalla un texto y tantas barritas como larga
sea la string
"""

def barras(x):
    for i in range(x):
        print("_", end =" ")

frase = input("Escribe : ")

barras(len(frase))