# Задача №35. 
# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым 
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число) 
# Input: 5 
# Output: yes

def prime_num(n):
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            return "NO"
    return "YES"

num = int(input("Введите число: "))
print(prime_num(num))




