# Задача №25. Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 
# Для решения данной задачи используйте функцию .split()

string = "a a a b c a a d c d d"
my_list = string.split()
result = {}

for el in my_list:
    if el not in result:
        print(el, end=" ")
        result[el] = 0
    else:
        result[el] += 1
        print(f"{el}_{result[el]}", end=" ")
