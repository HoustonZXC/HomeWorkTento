# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = -1
while number < 0:
    number = int(input('Введите положительное число: '))
max_answer = -1
while number > 10:
    number_cut = number % 10
    number = number // 10
    if number_cut > max_answer:
        max_answer = number_cut
print(f'Самая большая цифра в вашем числе: {max_answer}')
