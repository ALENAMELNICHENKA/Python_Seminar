# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input:  5 
# Output:  6
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89....и т.д.
# т.е. следующее число = сумме двух предыдущих

n = int(input("Введите чило: "))
fib_1 = 1
fib_2 = 2
count = 4

while fib_2 < n:
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    count = count + 1

if fib_2 != n:
    print("-1")
else:
    print(count)