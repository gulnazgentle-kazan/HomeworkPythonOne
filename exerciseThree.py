"""
Задача 3: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""

ticket = int(input("Введите шестизначный номер билета: "))

numberOne = ticket // 100000
numberTwo = ticket // 10000 % 10
numberThree = ticket // 1000 % 10
numberFour = ticket // 100 % 10
numberFive = ticket // 10 % 10
numberSix = ticket % 10
# Ищем сумму первых трех и следующих трех чисел
sumOne = numberOne + numberTwo + numberThree
sumTwo = numberFour + numberFive + numberSix

if (sumOne == sumTwo):
    print('yes')
else:
    print('no')
