"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора
@property.
"""

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @property
    @abstractmethod
    def sum_cloth_need(self):
        pass


class Clothes(AbstractClothes):
    total_cloth = []

    def __init__(self, measure):
        self.measure = measure

    @property
    def sum_cloth_need(self):
        return f'Всего ткани: \n{sum(self.total_cloth)}'


class Coat(Clothes):
    def __init__(self, measure):
        super().__init__(measure)

    def cloth_need(self):
        v = self.measure / 6.5 + 0.5
        self.total_cloth.append(v)
        return v

    def __str__(self):
        return f'Ткани для пальто размера {self.measure}: {self.cloth_need()}'


class Suit(Clothes):
    def __init__(self, measure):
        super().__init__(measure)

    def cloth_need(self):
        h = self.measure * 2 + 0.3
        self.total_cloth.append(h)
        return h

    def __str__(self):
        return f'Ткани для костюма размера {self.measure}: {self.cloth_need()}'


coat = Coat(52)
suit = Suit(170)
print(suit.cloth_need())
print(coat.cloth_need())
print(coat.sum_cloth_need)
