# Задача №47. 

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
'''Ввод:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print(‘ok’)
else:
    print(‘fail’)

Вывод: 
ok'''

#немного теории===============================================================

'''def my_lambda(x, y):
return x * y

my_lambda(2,3)

f = lambda x, y: x * y

f(2,3)'''
#=============================================================================

'''my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

res_list = filter(lambda x: x % 2 == 0, my_list)
print(*res_list)
print(list(res_list))'''
#=============================================================================

#Решение:

transformation = lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')