# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.

import random
some_list = [random.randint(1, 100) for i in range(1, 10)]
print(some_list)

some_list2 = [some_list[i] for i in range(1, len(some_list)) if some_list[i] > some_list[i - 1]]
print(some_list2)
