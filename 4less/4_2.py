"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых
больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования
списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def larger(arg_list):
    for index in range(1, len(arg_list)):
        if arg_list[index] > arg_list[index - 1]:
            yield arg_list[index]


input_list = list(map(int, input('Введите список через пробел: ').split()))
result_list = []
generator = larger(input_list)
for el in generator:
    result_list.append(el)
print(f'Результат: {result_list}')
