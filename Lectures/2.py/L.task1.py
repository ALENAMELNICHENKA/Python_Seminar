# List comprehension — это упрощенный подход к созданию списка, 
# который задействуетциклfor,а так же инструкции
# if-else для определения того,что в итоге окажется в финальном списке.

#Например:
#1. Простая ситуация — список: 
# list_1 = [exp for item in iterable]

#2. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]


# Задача:Создать список, состоящий из четных чисел в диапазоне от 1 до 100. 
# Решение: 
# 1. Создать список чисел от 1 до 100
list_1 = [] 
for i in range(1, 101): 
    list_1.append(i) 
    print(list_1)# [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
    list_1 = [i for i in range(1, 101)]# [1, 2, 3,...,100]