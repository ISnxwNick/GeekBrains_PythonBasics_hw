"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
try:
    my_list = list(map(int, input('Введите числа через пробел: ').split()))
    sum = 0
    with open('5.txt', 'w') as f:
        print('Введенные числа: ', end='', file=f)
        for el in my_list:  # Записываем введенный список в файл
            print(el, end=' ', file=f)
            sum += el
        print('\nСумма чисел:',sum, file=f)
    print('Сумма чисел:',sum)   #так и не понял на какой экран выводить, консоли или файла, вывел и там и там)
except ValueError:
    print('Вы ввели не число!')