'''Задача №43. 
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, 
которую необходимо посчитать. 
Вводится список чисел. 
Все числа списка находятся на разных строках. 
Ввод: 1 2 3 2 3
Вывод:  2'''

from random import randint

n = int(input("Введите размер списка: "))
my_list = [randint(1, 3) for _ in range(n)]
count = 0

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            count += 1

print(my_list)
print(count)