"""
O O O   · · ·
O O O   · · ·
O O O   · · ·
"""
import random


def draw():
    print("")
    for i in range(9):
        print(tablero[i] + " ", end="")
        if (i + 1) % 3 == 0:
            print("")
    print("")

def player(number):
    stop = False
    player_mov = ""
    while not stop:
        while not player_mov in cells:
            player_mov = input("Tu turno, jugador {}: ".format(number))
        if tablero[int(player_mov)-1] != vacio:
            player_mov = ""
        else:
            tablero[int(player_mov)-1] = number
            stop = True

def check(won):
    empty = 0
    for i in tablero:
        if i != vacio:
            empty += 1

    if empty == 9:
        won = 3

    """Horizontales"""
    if tablero[0] == tablero [1] and tablero[1] == tablero[2] and tablero[0] != vacio:
        won = int(tablero[0])
    if tablero[3] == tablero [4] and tablero[4] == tablero[5] and tablero[3] != vacio:
        won = int(tablero[3])
    if tablero[6] == tablero [7] and tablero[7] == tablero[8] and tablero[6] != vacio:
        won = int(tablero[6])
    """Verticales"""
    if tablero[0] == tablero [3] and tablero[3] == tablero[6] and tablero[0] != vacio:
        won = int(tablero[0])
    if tablero[1] == tablero [4] and tablero[4] == tablero[7] and tablero[1] != vacio:
        won = int(tablero[1])
    if tablero[2] == tablero [5] and tablero[5] == tablero[8] and tablero[2] != vacio:
        won = int(tablero[2])
    """Diagonales"""
    if tablero[0] == tablero [4] and tablero[4] == tablero[8] and tablero[0] != vacio:
        won = int(tablero[0])
    if tablero[2] == tablero [4] and tablero[4] == tablero[6] and tablero[2] != vacio:
        won = int(tablero[2])

    return won

exit = False
vacio = "0"
tablero = [vacio] * 9
cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
win = 0
print("\n3 en línea \n")
print("Las casillas se numeran del 1 al 9, de arriba a abajo y de izquierda a derecha\n")

for i in range(1, 10):
    print(str(i), end =" ")
    if i%3 == 0:
        print("")
print("\nEmpezamos")

turno = (random.randrange(2))

while not exit:
    draw()
    if turno == 0:
        player("1")
        turno = 1
    else:
        player("2")
        turno = 0

    win = check(win)
    if win == 3:
        print("EMPATE!!!")
        exit = True
    elif win != 0:
        draw()
        print("GANADOR, EL JUGADOR {}".format(win))
        exit = True





