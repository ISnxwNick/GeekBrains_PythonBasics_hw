"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию (проверку на корректность) числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

import re


class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def converter(cls, date_string):
        num = [int(i) for i in date_string.split('-')]
        print(f'День {num[0]}, месяц {num[1]}, год {num[2]}')

    @staticmethod
    def validator(date_string):
        try:
            num = [int(i) for i in re.split(r'-', date_string, maxsplit=2)]
        except ValueError:
            print('некорректное значение')
            return
        if num[0] in range(1, 32):
            print(f'день корректен: {num[0]}')
        else:
            print(f'день введен неверно!')
        if num[1] in range(1, 13):
            print(f'месяц корректен: {num[1]}')
        else:
            print('месяц введен неверно!')
        if num[2] > 0:
            print(f'год корректен: {num[2]}')
        else:
            print(f'год до н.э.!')


Date.converter('01-11-2003')
Date.validator('31-02-1025')
Date.validator('12--lkmsdfkl-45')
Date.validator('4-9--52')
