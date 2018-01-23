"""
Escribe una función que reciba una lista de números y devuelva otra, pero
conteniendo sólo los números pares
"""

def pares(lista):
    lista_pares = []
    for i in lista:
        if i%2 == 0:
            lista_pares.append(i)
    return lista_pares


lista_numeros = [2, 4, 5, 7, 1, 10, 9, 22, 23]

print(pares(lista_numeros))

