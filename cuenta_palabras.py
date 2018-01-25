"""
Crea un programa que cuente el número de veces que aparece una palabra en una string
"""

user_string = dict()

frase = input("Escribe una frase: ")
palabra = ""
contador = 0


for i in frase:
    if i != " ":
        palabra += i
        if contador == len(frase)-1:
            if palabra in user_string:
                user_string[palabra] += 1
            else:
                user_string[palabra] = 1
    else:
        if palabra in user_string:
            user_string[palabra] += 1
        else:
            user_string[palabra] = 1

        palabra = ""
    contador += 1

print(user_string)