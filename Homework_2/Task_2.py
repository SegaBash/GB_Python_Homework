# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z

print(f'X\tY\tZ\t¬(X ∧ Y) ∨ Z')
false_true = range(2)
for x in false_true:
    for y in false_true:
        for z in false_true:
            print(x, y, z, int(not (x and y) or z),  sep='\t')
