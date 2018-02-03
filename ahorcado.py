"""
    +-------+
    |       |
    |       0
    |      /|\
    |      / \
===============
┌───┐
JUEGO DEL AHORCADO
"""
import random

HANGMAN = ['''
    +-------+
    |        
    |        
    |          
    |          
===============''' ,
'''
    +-------+
    |       |
    |        
    |          
    |          
===============''',
'''
    +-------+
    |       |
    |       0
    |        
    |          
===============''',
'''
    +-------+
    |       |
    |       0
    |       |  
    |          
===============''',
'''
    +-------+
    |       |
    |       0
    |      /|  
    |          
===============''',
'''
    +-------+
    |       |
    |       0
    |      /|\ 
    |         
===============''',
'''
    +-------+
    |       |
    |       0
    |      /|\ 
    |      /   
===============''',
'''
    +-------+
    |       |
    |       0
    |      /|\ 
    |      / \ 
==============='''
]

WORDS = ["animal", "arbusto", "aeronave", "anfibio", "botella", "bisturi", "camioneta", "caravana", "cocinar", "caballo",
         "ordenador", "veterinario", "monitor", "baloncesto", "altavoz", "teclado", "internet", "colegio", "paraguas",
         "ahorcado", "juego", "drone", "castillo", "objetivo"]

"""7 OPORTUNIDADES"""


def draw_line():
    for i in range(len(word)):
        if user_word[i] == " ":
            print("_", end=" ")
        else:
            print(user_word[i], end=" ")
    print("\n")
    if len(user_letters)>0:
        print("Fallos: ")
        print(user_letters, end="\n\n")

def check_letter(letter):
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                user_word[i] = letter
    else:
        user_letters.append(letter)
        return False
    return True


level = 0
exit = 0
win = 0
word = WORDS[random.randrange(len(WORDS))].upper()
user_word = [" "]
user_letters = []

for i in word:
    user_word += " "
print("\n\nTienes que adivinar una palabra de {} letras".format(len(word)))

while exit == 0:
    print(HANGMAN[level],end="\n")
    draw_line()
    if not (check_letter(input("Letra: ").upper())) :
        level += 1
    else:
        ok = 0
        for i in range(len(word)):
            if user_word[i] == word[i]:
                ok += 1
        if ok == len(word):
            win = 1
            exit = True
    if level>6:
        win = 0
        exit = True

if win == 0:
    print(HANGMAN[level], end="\n")
    print("Has perdido!!!!! La palabra era {}".format(word))
else:
    draw_line()
    print("HAS GANADO!!!!")