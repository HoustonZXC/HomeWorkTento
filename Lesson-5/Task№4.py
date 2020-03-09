# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
translation = []
with open('test3.txt', 'r') as fool:
    for i in fool:
        i = i.split(' ', 1)
        print(i)
        translation.append(russian[i[0]] + ' ' + i[1])
with open('test4.txt', 'w') as cruel:
    cruel.writelines(translation)
