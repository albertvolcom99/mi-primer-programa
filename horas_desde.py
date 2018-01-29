"""
Crea un programa que te diga, introduciendo cualquier fecha, cuantas horas han pasado desde ese momento
"""

import datetime

date_day = int(input("Día : "))
date_month = int(input("Mes : "))
date_year = int(input("Año : "))
date = datetime.datetime(year=date_year, month=date_month, day=date_day)
now = datetime.datetime.now()

tiempo_pasado = now - date

print(tiempo_pasado.total_seconds()/3600)