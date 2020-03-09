# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def information(Name, LastName, byear, city, email, phone):
    print(Name, LastName, byear, city, email, phone)

information(Name = 'Pavel', LastName = 'Tumanov', byear = '1996', city = 'Moscow', email = '123@mail.ru', phone = '911')
information('pavel', 'tumanov', '1996', 'moscow', '123@mail.ru', '911')