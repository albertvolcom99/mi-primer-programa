"""
Crear un programa que al decirle el nombre de un color nos devuelva su traducción en inglés
"""

colores = dict()
exit = False

while not exit:

    opt = input("Consultar (C) / Salir (S): ").upper()

    if opt == "C":
        color = input("Color: ")
        if color in colores:
            print(colores[color])
        else:
            print("ERROR")
            print("El color no existe")
            opt  = ""
            while opt != "S" and opt != "N":
                opt = input("¿Desea añadirlo? S/N ").upper()
                if opt == "S":
                    colores[color] = input("{} en inglés es: ".format(color))

    elif opt == "S":
        exit = True

