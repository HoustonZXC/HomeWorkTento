# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(my_list)

some_number = int(input('Введите число '))

for el in range(len(my_list)):
    if my_list[el] == some_number:
        my_list.insert(my_list.count(some_number) + my_list.index(some_number), float(some_number))
        break
    elif my_list[0] < some_number:
        my_list.insert(0, some_number)
        break
    elif my_list[-1] > some_number:
        my_list.insert(-1, some_number)
        break
    elif my_list[el] > some_number and my_list[el + 1] < some_number:
        my_list.insert(el + 1, some_number)
        break
print(my_list)
