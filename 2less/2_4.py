'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с
новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
'''
my_list = input('Введите строку из слов разделенных пробелами:').split()
for index, var in enumerate(my_list):
    print(f'Номер строки: {index}, слово: {var[:10]}')
