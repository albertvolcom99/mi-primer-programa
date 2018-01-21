"""
Realizar el FizzBuzz con las mismas reglas, pero en el caso que el número sea divisible
entre 3 y 5, cambiar el texto por "Bazinga"
"""


numbers = [4, 3, 15, 5, 25, 30, 65, 34]

for i in range(len(numbers)):

    if numbers[i] % 3 == 0 and numbers[i]%5 == 0:
        numbers[i] = "Bazinga"
    elif numbers[i] % 3 == 0:
        numbers[i] = "Fizz"
    elif numbers[i] % 5 == 0:
        numbers[i] = "Buzz"

print(numbers)