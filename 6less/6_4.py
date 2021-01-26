"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn_right(self):
        return f'Машина {self.name} повернула направо'

    def turn_left(self):
        return f'Машина {self.name} повернула направо'

    @property
    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


class SportCar(PoliceCar):
    pass


class TownCar(PoliceCar):
    limit = 60
    car_class_name = 'городской машины(60)'

    def show_speed(self):
        if self.speed > self.limit:
            return f'Превышение {self.name} по скорости для {self.car_class_name}, скорость: {self.speed}'
        else:
            return f'Машина {self.name} едет со скоростью {self.speed}'


class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        self.limit = 40
        self.car_class_name = 'рабочей машины(45)'


Mercedes = SportCar(120, 'Черный', 'Mercedes', False)
Kamaz = WorkCar(45, 'Белый', 'Kamaz', False)
Ford = TownCar(55, 'Зеленый', 'Ford', False)
Lada = PoliceCar(70, 'Синий', 'Lada', True)
print(Mercedes.turn_left(), Lada.go())
print(Lada.police())
print(Ford.stop(), Kamaz.police())
print(Mercedes.show_speed)
print(Ford.show_speed())
print(Kamaz.show_speed())
