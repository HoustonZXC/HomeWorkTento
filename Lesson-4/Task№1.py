# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.


def money():
    try:
        time = float(input('Время работы в часах: '))
        salary = int(input('Ставка за час в рублях: '))
        premiaaa = int(input('Премия в рублях, если имеется: '))
        bruh = time * salary + premiaaa
        print(f'Зарпалата будет равна:{bruh} руб.')
    except ValueError:
        return print('Вводить можно только числа.')


if __name__ == '__main__':
    money()
