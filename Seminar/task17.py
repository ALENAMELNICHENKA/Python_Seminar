# # Задача №17. Решение в группах Дан список чисел. 
# Определите, сколько в нем встречается различных (нет повторов) чисел. 
# Input: [1, 1, 2, 0, -1, 3, 4, 4] 
# Output: 6

import random

size = int(input("Введите размер списка: "))
list_1 = []

for _ in range(size):
    num = random.randint(1, 5)
    list_1.append(num)
print(list_1)

