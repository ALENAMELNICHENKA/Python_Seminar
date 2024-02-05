# Задача №37. Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и использовать циклы 
# (даже для ввода и вывода).
# Input:    5 -> 1 2 3 4 5 
# Output: 5 4 3 2 1
def reversed(num):
    el = input("Введите число: ")
    if num == 1:
        print(el, end=" ")
        return
    reversed(num - 1)
    print(el, end=" ")
    
n = int(input("Введите количество чисел последовательности: "))
reversed(n)