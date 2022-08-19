# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2


def letter_count(first_str, second_str):
    out = ''
    sep = ''
    for i in first_str:
        count = 0
        for j in second_str:
            if i == j:
                count += 1
        out += sep
        out += f'{i} - {count}'
        sep = ', '
    return out

first_str = 'one'
second_str = 'onetwonine'
print(letter_count(first_str,second_str))