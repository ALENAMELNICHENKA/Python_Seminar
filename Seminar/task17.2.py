# №Задача 17. 
# Определите, сколько в нем встречается различных (нет повторов) чисел. 
# Input: [1, 1, 2, 0, -1, 3, 4, 4] 
# Output: 6

#С помощью функции List comprehension — это упрощенный подход к созданию списка

import random

size = int(input("Введите размер списка: "))
list_1 = [random.randint(1, 5) for _ in range(size)]

print(list_1)

#1 Решение:
# Решаем через множество (set())...

print(len(set(list_1)))



#2 Решение без использования множества:

unique = []
for num in list_1:
    if num not in unique:
       unique.append(num)
print(len(set(list_1)))