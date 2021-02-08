from time import sleep
from itertools import cycle
from threading import Thread


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

    def _running(self):
        while True:
            # print(f'Горит {self.current_color}, задержка {self.current_time}')
            # sleep(self.current_time)
            self.current_color = next(self.colors)
            self.current_time = next(self.timer)
            print('Всё ок, переключаюсь')

    def running(self):
        Thread(target=self._running).start()

    def check(self):
        while True:
            if self.current_color == self.current_color:
                print(f'Горит {self.current_color}, задержка {self.current_time}')
            else:
                print('Нарушен порядок светофора!')
                raise SystemExit
            sleep(self.current_time)


a = TrafficLight()
a.check()
a.running()
