# Задача №19. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо,  K – положительное число. 
# Input:   [1, 2, 3, 4, 5] 
# k = 3 
# Output:  [3, 4, 5, 1, 2]

#1 Решаем с помощью среза:

n = int(input("Введите количество целых чисел: "))

numbers = [i for i in range(1, n+1)]
print(numbers)
k = int(input("Введите К: "))
print(numbers[-k:] + numbers[:-k])


#1 Решаем с помощью метода pop:

for _ in range(k):
    last_num = numbers.pop()
    numbers.insert(0, last_num)
print(numbers)