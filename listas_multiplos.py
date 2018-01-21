"""
Crear un programa que guarde e imprima varias listas con todos los números
que estén dentro de una lista proporcionada por el usuario y
sean múltiplos de 2, de 3, de 5 y de 7
"""


lista_numbers = []
numero = 1

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

while numero!=0:
    numero = "a"
    while numero.isdigit()==False:
        numero = input("Introduce un nunero a la lista (0 para acabar): ")
    numero = int(numero)
    if numero!=0:
        lista_numbers.append(numero)

for i in lista_numbers:
    if i % 2 == 0:
        multiplos_dos.append(i)
    if i % 3 == 0:
        multiplos_tres.append(i)
    if i % 5 == 0:
        multiplos_cinco.append(i)
    if i % 7 == 0:
        multiplos_siete.append(i)


print("Números múltiplos de 2: ")
print(multiplos_dos)
print("")
print("Números múltiplos de 3: ")
print(multiplos_tres)
print("")
print("Números múltiplos de 5: ")
print(multiplos_cinco)
print("")
print("Números múltiplos de 7: ")
print(multiplos_siete)



