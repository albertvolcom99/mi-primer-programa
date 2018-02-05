"""
Escribe una frase aleatoria de una lista de strings cada 3 segundos
"""

import time
import datetime
import random

text_list = ["Frase 1", "Frase 2", "Frase 3", "Frase 4", "Frase 5", "Frase 6", "Frase 7"]


def main():
    while True:
        print(text_list[random.randrange(len(text_list))])
        time.sleep(3)



if __name__  == "__main__":
    main()