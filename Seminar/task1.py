# Задача №1.  За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной конструкцией if и циклами.
# Input:
# n = 700км/д
# s= 750км
# Output: 2

import math #импортируем библиотеку math


distance = int(input("Введите длину маршрута: "))
speed = int(input("Введите скорость км в день: "))
day = math.ceil(distance / speed)
print(day)



#2

distance = int(input("Введите длину маршрута: "))
speed = int(input("Введите скорость км в день: "))
day = (distance + (speed - 1)) // speed
print(day)