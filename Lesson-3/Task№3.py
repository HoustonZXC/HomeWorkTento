# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    y = (arg1, arg2, arg3)
    y = list(y)
    minimum = min(arg1, arg2, arg3)
    y.remove(minimum)
    x = y[0] + y[1]
    return x

print(my_func(8, 2, 3))
