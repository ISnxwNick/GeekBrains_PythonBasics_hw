"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, hours, salary, bonus = argv
print('Имя скрипта:', script_name)
print(f'Заработная плата: {int(hours)} * {int(salary)} + {int(bonus)}={hours * salary + bonus}')
'''
Протестировать через ком. строку не вышло, буду разбираться дальше, сделал по образцу с методички, прошу прощения за задержку в выполнении заданий
'''