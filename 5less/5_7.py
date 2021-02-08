"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

sum_profit = count = 0
firm_dict = avg_dict = {}
result_list = []
with open('7_source.txt', 'r', encoding='utf-8') as file_r:
    with open('7_json.json', 'w') as file_w:
        for line in file_r:
            my_list = line.split()
            income = int(my_list[2])
            costs = int(my_list[3])
            if income >= costs:
                profit = income - costs
                sum_profit += profit
                count += 1
                firm_dict.update({my_list[0]: profit})
                print(f'Фирма: {my_list[0]}, форма собственности: {my_list[1]}, выручка: {my_list[2]},'
                      f' издержки: {my_list[3]}, прибыль: {profit}')
            else:
                losses = costs - income
                print(f'Фирма: {my_list[0]}, форма собственности: {my_list[1]}, выручка: {my_list[2]},'
                      f' издержки: {my_list[3]}, убытки: {-losses}')
                firm_dict.update({my_list[0]: -losses})
        print(f'Средняя прибыль: {sum_profit / count}')
        avg_dict = {"average_profit": sum_profit / count}
        result_list.append(firm_dict)
        result_list.append(avg_dict)
        json.dump(result_list, file_w)
