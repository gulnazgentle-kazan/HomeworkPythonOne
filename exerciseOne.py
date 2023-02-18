"""
Задача 1: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""


number = int(input('Введите любое трехзначное число: '))

if number < 100 or number > 999:
    print('Введено некорректное число')
else:
    numberOne = number % 10
    numberTwo = number // 10 % 10
    numberThree = number // 100 % 10
    print(numberOne + numberTwo + numberThree)
