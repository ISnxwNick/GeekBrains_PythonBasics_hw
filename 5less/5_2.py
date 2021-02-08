"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
with open(r'2.txt', 'w') as f:
    lines = 0
    not_empty = True
    while not_empty:
        words = 0
        my_string = list(map(str, input('Введите строку: ').split()))
        if my_string:
            lines += 1
            f.write(f"Введенная строка: {' '.join(map(str, my_string))}")
            f.write(f'\nКоличество слов в строке: {len(my_string)}\n')
        else:
            not_empty = False
    f.write(f'\nКоличество введенных строк: {lines}')
