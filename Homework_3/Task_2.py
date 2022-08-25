# В файле находятся названия фруктов.Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def First_letter_list(letter, word_list):
    out_list = []
    for i in word_list:
        if str.lower(i[0]) == str.lower(letter):
            out_list.append(i)
    return out_list

letter = input("Введите букву ")
data = open('Homework_3/fruit.txt', 'r',  encoding='utf8')
fruits = data.read().split('\n')
data.close
result_list = First_letter_list(letter, fruits)
print(f'Фрукты на "{letter}" :')
print(str.join('\n', result_list))
