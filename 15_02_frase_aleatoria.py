"""
Escribe un programa que imprima por pantalla una frase aleatoria cada segundo.
La lista de frases de la que se seleccionará la frase aleatoria será distinta según el segundo
en el que estemos
Segundos acabados en 0 : frases alegres
Segundos acabados en 1 : nombres de muebles
Segundos acabados en 2 : nombres de bebidas
Segundos acabados en 3 : frases de odio
Segundos acabados en 4 : nombres de comida
Segundos acabados en 5 : frases absurdas
Segundos acabados en 6 : nombres de animales
Segundos acabados en 7 : frases motivacionales
Segundos acabados en 8 : sonidos de animales
Segundos acabados en 9 : frases tristes
"""


import time
import random
import datetime

LIST_ZERO = ["frase alegre 1", "frase alegre 2", "frase alegre 3", "frase alegre 4", "frase alegre 5"]
LIST_ONE = ["mueble 1", "mueble 2", "mueble 3", "mueble 4", "mueble 5", "mueble 6"]
LIST_TWO = ["bebida 1", "bebida 2", "bebida 3", "bebida 4", "bebida 5", "bebida 6", "bebida 7"]
LIST_THREE = ["odio 1", "odio 2", "odio 3", "odio 4"]
LIST_FOUR = ["comida 1", "comida 2", "comida 3", "comida 4", "comida 5"]
LIST_FIVE = ["absurdo 1", "absurdo 2", "absurdo 3", "absurdo 4", "absurdo 5", "absurdo 6"]
LIST_SIX = ["animales 1", "animales 2", "animales 3", "animales 4", "animales 5"]
LIST_SEVEN = ["motivacional 1", "motivacional 2", "motivacional 3", "motivacional 4", "motivacional 5", "motivacional 6"]
LIST_EIGHT = ["animal 1", "animal 2", "animal 3", "animal 4", "animal 5"]
LIST_NINE = ["triste 1", "triste 2", "triste 3", "triste 4", "triste 5", "triste 6"]


def print_list(list):
    print(list[random.randrange(len(list))])
    time.sleep(1)

def main():
    while True:
        current_time = datetime.datetime.now()
        current_second = int(str(current_time.second)[-1])
        if current_second == 0:
            print_list(LIST_ZERO)
        elif current_second == 1:
            print_list(LIST_ONE)
        elif current_second == 2:
            print_list(LIST_TWO)
        elif current_second == 3:
            print_list(LIST_THREE)
        elif current_second == 4:
            print_list(LIST_FOUR)
        elif current_second == 5:
            print_list(LIST_FIVE)
        elif current_second == 6:
            print_list(LIST_SIX)
        elif current_second == 7:
            print_list(LIST_SEVEN)
        elif current_second == 8:
            print_list(LIST_EIGHT)
        elif current_second == 9:
            print_list(LIST_NINE)



if __name__ == "__main__":
    main()