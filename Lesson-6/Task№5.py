# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')

number1 = Stationery('Ручка')
Pen.draw(number1)

number2 = Stationery('Карандаш')
Pencil.draw(number2)

number3 = Stationery('Маркер')
Handle.draw(number3)

bruh = Stationery('Что угодно')
Stationery.draw(bruh)