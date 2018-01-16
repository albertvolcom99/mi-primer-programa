"""
Ordenar numeros
"""

numeros = []
exit = False

while not exit:
    numeros.append(int(input("Dime un número (0 para acabar): ")))
    if numeros[-1] == 0:
        exit = True
        numeros.pop(-1)

for x in range(len(numeros)):
    for i in (range(len(numeros)-1)):
        if numeros[i] > numeros[i + 1]:
            numeros.insert(i+2, numeros[i])
            numeros.pop(i)
        print(numeros)

for i in numeros:
    print(str(i), end=" ")