# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

quater = int(input('Введите номер четверти '))
if quater == 1:
    print('x > 0, y > 0')
elif quater == 2:
    print('x < 0, y > 0')
elif quater == 3:
    print('x < 0, y < 0')
elif quater == 4:
    print('x > 0, y < 0')
else:
    print('Это какая то неправильная четверть')
