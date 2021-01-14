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
            for word in my_string:
                words += 1
            lines += 1
            f.write(f"Введенная строка: {' '.join(map(str, my_string))}")
            f.write(f'\nКоличество слов в строке: {words}\n')
        else:
            not_empty = False
    f.write(f'\nКоличество введенных строк: {lines}')
