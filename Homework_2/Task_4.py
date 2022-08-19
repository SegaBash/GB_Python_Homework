# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.

# 3 -> [2, 3, -3, -2, -1, 0, 1]


def create_list(length):
    lst = [0] * (2 * length + 1)
    k = 0
    for i in range(-length, length+1):
        lst[k] = i
        k += 1
    return lst

def shift_list(lst, shift):
    lst_2 = lst.copy()
    for i in lst:
        lst_2[i] = lst[i-shift]
    return lst_2
    


n = int(input('Введите число '))
list_1 = create_list(n)
list_2 = shift_list(list_1, 2)
print('Исходный массив:', list_1, sep='\n')
print('Смещенный массив:', list_2, sep='\n')