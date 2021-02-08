"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
(запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав
экземпляр и вызвав описанный метод.
Задачу можно усложнить, введя переключение цветов в отдельном потоке (С помощью класса Threads)и реализовав
проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
Подсказка: Подтверждения переключение можно показать вызовом print(self.color) через заданные промежутки
времени для каждого цвета.
"""
from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__condition = {
            'красный': 6,
            'желтый': 2,
            'зеленый': 8
        }
        self.colors = cycle(self.__condition.keys())
        self.current_color = next(self.colors)
        self.timer = cycle(self.__condition.values())
        self.current_time = next(self.timer)

    def running(self):
        while True:
            print(f'Горит {self.current_color}, задержка {self.current_time}')
            sleep(self.current_time)
            self.current_color = next(self.colors)
            self.current_time = next(self.timer)


a = TrafficLight()
a.running()
