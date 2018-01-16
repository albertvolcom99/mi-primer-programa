"""
Fibonacci
"""

resp_posible = ["SI", "NO"]
resp = ""

while resp != "NO":
    tot = 0
    num_a = 0
    num_b = 1
    resp = ""
    while tot<1:
        tot = (int(input("¿Cuantos números de Fibonacci quieres? (Mínimo 3): ")) - 2)

    print(num_a)
    print(num_b)

    for i in range(tot):
        num_b += num_a
        num_a = num_b - num_a
        print(num_b)

    while not resp in resp_posible:
        resp = input("¿Otra vez? ( SI/NO): ").upper()


