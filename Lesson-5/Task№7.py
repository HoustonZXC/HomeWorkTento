# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

bruh = []
with open('test_bruh.txt', 'w') as fool:
    with open('test7.txt') as fool2:
        money = {}
        for i in fool2:
            money[i.split()[0]] = int(i.split()[2]) - int(i.split()[3])

        sr_znach = sum([int(i) for i in money.values() if int(i) > 0]) / len(
            [int(i) for i in money.values() if int(i) > 0])
        bruh.append(money)
        bruh.append({'sr_znach': sr_znach})
    json.dump(bruh, fool)
