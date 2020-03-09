# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('test2.txt', 'r') as fool:
    my_list = fool.read().split('\n')
    my_list_2 = []
    my_list_3 = []
    print(my_list)
    for i in my_list:
        z = i.split()
        my_list_3.append(int(z[1]))
        if int(z[1]) < 20000:
            my_list_2.append(z[0])
        else:
            pass
    sr_znach = sum(my_list_3)/len(my_list_3)
    print(f'Список тех чья зарплата меньше 20000: {my_list_2}')
    print(f'Средняя величина дохода составляет: {sr_znach}')
