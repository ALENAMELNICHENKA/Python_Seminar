'''Хакер Василий получил доступ к классному журналу 
и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот:
 все максимальные – на минимальные. 
 Input: 5 -> 1 3 3 3 4 
 Output: 1 3 3 3 1'''

from random import randint

def max_to_min(list_nums):
    max_num = max(list_nums)
    min_num = min(list_nums)
    while max_num in list_nums:
        i_max_num = list_nums.index(max_num)
        list_nums[i_max_num] = min_num
    
n = int(input("Введите количество оценок: "))
# marks = []

# for _ in range(n):
#     marks.append(randint(1, 5))

marks = [randint(1, 5)for _ in range(n)]
print(marks)

max_to_min(marks)
print(marks)