"""
Crea un programa que pregunte al usuario que adivine un número del 1 al 10,
pero ese número se va a generar aleatoriamente.
Hacer esperar 3 segundos antes de dar la respuesta
"""

import random
import time


random_number = random.randrange(10)+1

def main():
    exit = False
    while not exit:
        user_number = int(input("Dime un número del 0 al 10 : "))
        if user_number == random_number:
            print("HAS GANADO")
            exit = True
        else:
            time.sleep(3)

if __name__ == "__main__":
    main()