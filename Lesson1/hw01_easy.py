﻿
__author__ = 'Укладников Андрей'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).   z
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).

isCorrectInput = False
n = 0
while isCorrectInput == False :
    try:
        n = int(input("Введите целое число:"))
        isCorrectInput = True
    except:
        print("Вы ввели не целое число.")

#print(type(n))
s = str(n)
print("введенное число: ",s)
i = 0
while i < len(s):
    print("цифра на позиции:",i," = ",s[i])
    i += 1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.

v1 = input("Введите первое значение:")
v2 = input("Введите второе значение:")
n = v1
v1 = v2
v2 = n
print("первое значение:",v1)
print("второе значение:",v2)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

isCorrectAge = False
age = 0
while isCorrectAge == False :
    try:
        age = float(input("Введите возраст:"))
        isCorrectAge = True
    except:
        print("Вы ввели не целое число.")

if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")



