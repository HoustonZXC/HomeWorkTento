# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('my_text.txt', 'w') as fool:
    my_list = []
    smth = input('Введите что-нибудь: ')
    while smth:
        my_list.append(smth + '\n')
        smth = input('Введите что-нибудь: ')
    fool.writelines(my_list)

