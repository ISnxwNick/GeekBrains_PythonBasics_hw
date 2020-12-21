'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
'''
method = input('Нажмите l для реализации со списком или d для реализации со словарем: ')
if method == 'l':
    month = int(input('Введите номер месяца(1..12): '))
    year = ['Зима', 'Весна', 'Лето', 'Осень']  # Может есть способ красиво решить через списки?
    if month in range(1, 3) or month == 12:
        print(year[0])
    elif month in range(3, 6):
        print(year[1])
    elif month in range(6, 9):
        print(year[2])
    elif month in range(9, 12):
        print(year[3])
elif method == 'd':
    month = int(input('Введите номер месяца(1..12): '))
    year = {
        'Зима': (1, 2, 12),
        'Весна': (3, 4, 5),
        'Лето': (6, 7, 8),
        'Осень': (9, 10, 11)
    }
    for key in year.keys():
        if month in year[key]:
            print(key)
