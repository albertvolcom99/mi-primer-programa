"""
Escribe una función que encuentre el número más grande entre 3
"""


def mayor(lista):
    max_number = lista[0]
    for i in lista:
        if i>max_number:
            max_number = i

    return max_number

lista_numeros = [5, 2, 1]

print("El número más grande es {}".format(mayor(lista_numeros)))

