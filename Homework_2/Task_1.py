# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

n = int(input('Введите число '))
fac_list = [0] * n

for i in range(n):
    fac_list[i] = factorial(i + 1)
print(fac_list)


