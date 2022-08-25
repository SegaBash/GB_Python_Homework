# Создайте файл. Запишите в него N первыхэлементов последовательности Фибоначчи.
#

def Fibo(n):
    fibo = [1] * n
    prev_value = current_value = 1
    for i in range(2, n):
        current_value, prev_value = prev_value + current_value, current_value
        fibo[i] = current_value
    return fibo

n = int(input("Введите количество чисел Фибоначчи "))
if n > 100:
    print('Сам(a) считай!')
    exit
data = open('Homework_3/out.txt', 'w')
data.write(str(Fibo(n)))
data.close

