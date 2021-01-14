"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
my_dict = {}
my_list = []
sum_salary = staff = count = 0
with open('3.txt', 'r') as f:
    for line in f:  # считываем файл в список списков
        my_list.append(line.split())
my_dict = dict(my_list)  # преобразовываем в словарь
my_dict = {man: int(salary) for man, salary in my_dict.items()}  # преобразовываем значения словаря в int

print('Список людей с окладом менее 20(тыс.): ')
for man in my_dict:  # Далее работа со словарем
    salary = my_dict.get(man)
    sum_salary += salary
    if salary < 20:
        count += 1
        print(f'{count})Фамилия: {man}, оклад: {salary}')
    staff += 1
print(f'Средняя величина дохода сотрудников(тыс.): {sum_salary / staff}')
