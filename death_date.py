import datetime
import random

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 7
DRINKER_PENALIZATION = 5
SEDENTARY_PENALIZATION = 3

def print_with_uderscores(message):
    print(message)
    print(len(message) * "-")

def ask_yes_or_not(message):
    response = None
    while response != "S" and response != "N":
        response = input(message + " (S/N) : ").upper()
    return response == "S"

print_with_uderscores("¡Averigua cuánto te queda de vida!")
print("Completa esta encuesta para saber cuánto tiempo de vida te queda")

birth_date = input("¿Cuál es tu fecha de nacimiento (dd/mm/yyyy) ? : ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
years_lost = 0

if ask_yes_or_not("¿Fumas?"):
    years_lost += SMOKER_PENALIZATION

if ask_yes_or_not("¿Bebes?"):
    years_lost += DRINKER_PENALIZATION

if not ask_yes_or_not("¿Haces deporte?"):
    years_lost += SEDENTARY_PENALIZATION

base_lifespan = random.random() * AVERAGE_LIFESPAN / 2 + AVERAGE_LIFESPAN / 2

lifespan = base_lifespan - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()
days_to_death = int(days_to_death.total_seconds()/86400)

if days_to_death < 366:
    print("Te quedan {} días.".format(days_to_death))
else:
    print("Te quedan {} años.".format(int(days_to_death/365)))
