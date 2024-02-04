'''Задача №29. Решение в группах Ваня и Петя поспорили, 
кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента последовательности, 
которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.'''
#Ваня:
# n = int(input())
# max_number = - 1 #1 Ошибка №1. Было: max_number = 1000
# while n != 0:   
#     n = int(input())   
#     if max_number < n:  #2 Ошибка №2: if max_number > n:     
#     max_number = n 
# print(max_number)

#Петя: 

n = int(input())
max_number = -1 
while n != 0:        #2 while n < 0:
    if max_number < n:      
         max_number = n #3 n = max_number 
    n = int(input()) #1 Перенесли строку в блок if
print(max_number) #4 print(n)