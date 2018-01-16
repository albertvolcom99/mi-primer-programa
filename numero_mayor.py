
print("Tienes que decirme 10 números y yo te devolveré el mayor")
mayor = 0
for i in range(10):
    user_number = int(input("Numero: "))
    if user_number > mayor:
        mayor = user_number

print ("El mayor es {}".format(mayor))
