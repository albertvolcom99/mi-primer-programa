"""
Crea un programa que te diga cuánto falta para tu cumpleaños
y qué día de la semana será
"""
import datetime


dia_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

birthday_date_day = int(input("Fecha de tu cumpleaños (Día) : "))
birthday_date_month = int(input("Fecha de tu cumpleaños (Mes) : "))
birthday_date_year = int(input("Fecha de tu cumpleaños (Año) : "))

birthday_date = datetime.datetime(year=birthday_date_year, month=birthday_date_month, day=birthday_date_day)
now = datetime.datetime.now()
birthday_date = datetime.datetime(year=now.year, month=birthday_date_month, day=birthday_date_day)
rest = birthday_date - datetime.datetime.now()
dias = int(rest.days)
if dias < 0:
    dias += 365

print("Quedan {} días para tu cumpleaños".format(dias))

print("Y va a ser {}". format(dia_semana[birthday_date.weekday()]))
