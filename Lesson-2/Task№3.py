# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_input = int(input('Введите месяц в формате целового числа: '))

spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [12, 1, 2]

if user_input in spring:
    print('spring')
elif user_input in summer:
    print('summer')
elif user_input in autumn:
    print('autumn')
elif user_input in winter:
    print('winter')
else:
    print('Под таким номером нет месяца')

year = {
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10, 11),
    'winter': (12, 1, 2)
}

for key in year.keys():
    if user_input in year[key]:
        print(key)
