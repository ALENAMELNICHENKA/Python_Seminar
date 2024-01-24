# Задача №23. 
# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3] 
# Output: 2 (-1 < 5, 2 < 3) 
# Примечание: Пользователь может вводить значения списка или список задан изначально.

from random import randint

size = int(input("Введите размер массива: "))
numbers = []

for _ in range(size):
    numbers.append(randint(-5, 5))
print(numbers)


count = 0

for i in range(size - 1):
   if numbers[i] < numbers[i + 1]:
       count += 1
print(count)
