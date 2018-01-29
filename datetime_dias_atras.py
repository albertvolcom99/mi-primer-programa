"""
Crea un programa que te diga la fecha de hace 5 días respecto a hoy, y el día de la semana
"""

import datetime

fecha_hoy = datetime.datetime.now()
atras = int(input("Cuantos días atrás? : "))
dia_fecha_anterior = fecha_hoy + datetime.timedelta(days = -atras)

print(dia_fecha_anterior)

dia_semana = (dia_fecha_anterior.weekday())

dia_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print(dia_semana[dia_fecha_anterior.weekday()])