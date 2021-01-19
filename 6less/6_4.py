"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

# class Car:
#     def __init__(self, speed, color, name, is_police: bool):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = True if is_police else False
#     def go(self):
#         return 'Машина поехала'
#     def stop(self):
#         return 'Машина остановилась'
#     def direction(self):
#         pass
#     def show_speed(self):
#         return f'Машина едет со скоростью {self.speed}'
# class TownCar(Car):
#     def.is_police