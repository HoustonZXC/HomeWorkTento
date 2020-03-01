# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

for el in count(int(input('Введите число: '))):
    print(el)

my_list = [1, 3, 4, 'true', 'false', True, False]
for el in cycle(my_list):
    print(el)
