"""
Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento
"""

exit = False
agenda = dict()

while not exit:

    opt = input("Añadir (A) / Consultar (C) / Salir (S): ").upper()

    if opt == "A":
        nombre = input("Nombre: ")
        fecha = input("Fecha: ")
        agenda[nombre] = fecha
        print ("Ok")
    elif opt == "C":
        nombre = input("Nombre: ")
        print(agenda[nombre])
    elif opt == "S":
        exit = True


