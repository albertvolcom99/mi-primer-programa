"""
Escribe un texto al revés en clave
"""

texto_original = input("Introduce un texto: ")
volteado = ""

for i in range(len(texto_original)-1, -1 , -1):
    if texto_original[i].upper() == "A":
        volteado += "4"
    elif texto_original[i].upper() == "E":
        volteado += "3"
    elif texto_original[i].upper() == "I":
        volteado += "1"
    elif texto_original[i].upper() == "O":
        volteado += "0"
    elif texto_original[i].upper() == " ":
        volteado += "#"
    else:
        volteado += texto_original[i]

print(volteado)