# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Скорость авто: {self.speed}')

class TownCar(Car):
    def __init__(self):
        self.is_police = False

    def show_speed(self):
        print(f'Скорость авто: {self.speed}')
        if self.speed > 60:
            print('Внимание! Скорость превышает 60 км/ч')

class WorkCar(Car):
    def __init__(self):
        self.is_police = False

    def show_speed(self):
        print(f'Скорость авто: {self.speed}')
        if self.speed > 40:
            print('Внимание! Скорость превышает 40 км/ч')

class SportCar(Car):
    def __init__(self):
        self.is_police = False

class PoliceCar(Car):
    def __init__(self):
        self.is_police = True

work1 = Car(45, 'Синий', 'Mazda', False)
work1.go()
WorkCar.show_speed(work1)

sport1 = Car(120, 'Белый', 'Ferrari', False)
sport1.go()
sport1.show_speed()
sport1.stop()

town1 = Car(67, 'Черный', 'BMW', False)
town1.go()
TownCar.show_speed(town1)
town1.stop()

police1 = Car(80, 'Синий', 'Lada', True)
PoliceCar.go(police1)
PoliceCar.show_speed(police1)