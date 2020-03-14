# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractclassmethod

class clothes(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def result1(self, smth):
        pass

    @property
    def result2(self, smth2):
        pass

    @property
    def results(self):
        return self.result1 + self.result2

class pal(clothes):
    def __init__(self, name, razmer):
        super().__init__(name)
        self.razmer = razmer

    @property
    def rasxod(self):
        clothes.result1 = (round(self.razmer/6.5 + 0.5))
        return round(self.razmer/6.5 + 0.5)

class cos(clothes):
    def __init__(self, name, rost):
        super().__init__(name)
        self.rost = rost

    @property
    def rasxod(self):
        clothes.result2 = (self.rost * 2 + 0.3)
        return self.rost * 2 + 0.3

bruh = pal('Пальто1', 12)
print(f'{bruh.rasxod}')
bruh2 = cos('Костюм1', 4)
print(f'{bruh2.rasxod}')
bruh3 = clothes('result')
print(f'{bruh3.results}')