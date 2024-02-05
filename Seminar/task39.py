'''Задача №39.
Даны два массива чисел. Требуется вывести те элементы первого массива 
(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
Пользователь вводит  число N - количество элементов в первом массиве, 
затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
Затем элементы второго массива.
Ввод: 7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Вывод:  3 3 2 12    (каждое число вводится с новой строки)'''

from random import randint

n = int(input("Введите длину 1го массива: "))
n = int(input("Введите длину 2го массива: "))

# list1 = []
# list2 = []

# for i in range(n):
#     list1.append(randint(1, 10))

list1 = [randint(1, 10) for i in range(n)] # с помощью List comprehension
print(list1)

# for i in range(n):
#     list2.append(randint(1, 10))

list2 = {randint(1, 10) for i in range(n)} # с помощью List comprehension
print(list2)

res_list = []

for num in list1:
    if num not in list2:
        res_list.append(num)
        print(num, end=" ")