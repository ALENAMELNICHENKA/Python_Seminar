'''Задача №45. Два различных натуральных числа n и m называются дружественными, 
если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
Программа получает на вход одно натуральное число k, не превосходящее 105. 
Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
Пары необходимо выводить по одной в строке, разделяя пробелами. 
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
Ввод: 300
Вывод: 220  284

Пример: Возьмем 2 числа 220 и 284. Найдем их делители
Делители 220 - (1,2,4,5,10,11,20,22,44,55,110), если их сложить получится:
1+2+4+5+10+11+20+22+44+55+110 = 284
Делители 284 - (1,2,4,71,142)
1+2+4+71+142 = 220'''

def sum_div(num):
    summa = 1
    for div in range(2, num):
        if num % div == 0:
            summa += div
    return summa
    #return sum(div for div in range(1, num) if num % div == 0)
k = int(input("Введите число: "))        

for num_1 in range(2, k + 1):
    num_2 = sum_div(num_1)
    if num_1 < num_2 and num_1 == sum_div(num_2) and num_2 <= k:
        print(num_1, num_2)