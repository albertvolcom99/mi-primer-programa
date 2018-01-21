"""
Crear un programa que le repita al usuario todo lo que dice pero con todas
las vocales cambiadas por "i"
"""

exit = False
vocales = ["a", "e", "i", "o", "u"]

while exit == False:
    texto = input("Escribe (FIN para acabar): ")
    if texto.upper() == "FIN":
        exit = True
    else:
        for i in vocales:
            texto = texto.replace(i, "i")

        print(texto)

print("ADIOS")
