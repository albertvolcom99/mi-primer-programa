"""
Escribe una función que dado un número y un rango (otros 2 números), compruebe que ese número está
dentro del rango
"""

def rango(numero, rango_inf, rango_sup):
    if numero>= rango_inf and numero<=rango_sup:
        return True
    else:
        return False


print(rango(5,2,8))
