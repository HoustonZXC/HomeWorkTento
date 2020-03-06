# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('test.txt', 'r') as fool:
    my_list = fool.readlines()
    print(my_list)
    print(f'Количество позиций в файле: {len(my_list)}')
    for i in range(len(my_list)):
        print(len(my_list[i]) - 1)   # за вычетом \n

