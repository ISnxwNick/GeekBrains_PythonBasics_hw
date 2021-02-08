"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    a = [*args]
    a.sort()
    summa = a[-2] + a[-1]
    return f'Сумма наибольших 2х аргументов: {summa}'


try:
    x, y, z = map(int, input('Введите 3 числа через пробел: ').split())
    print(my_func(x, y, z))
except ValueError:
    print('Вы ввели не число')
