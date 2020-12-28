"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func1(x, y):
    res = x ** y
    return print(f'Результат возведения {x} в степень {y}: {res}')


def my_func2(x, y):
    temp = 1
    for i in range(-y):
        temp *= x
    res = 1 / temp
    return print(f'Результат возведения {x} в степень {y}: {res}')


def my_func3(x, y):
    if y == 0:
        return 1
    return x * my_func3(x, y + 1)  # глубина меняется со знаком + тк инверсия с отрицательным y


x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print('Введите способ цифрой:\n1.Через **\n2.Через цикл\n3.Рекурсивно')
method = int(input())
if method == 1:
    my_func1(x, y)
elif method == 2:
    my_func2(x, y)
elif method == 3:
    print(f'Результат возведения {x} в степень {y}: {1 / my_func3(x, y)}')
