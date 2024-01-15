a = 'python'
b = 'Привет, меня зовут Вася!'
z = 'Hello world!'
age = 25

# print(a, b, z)
# print(a, b, z, sep=' ', end='\n')

# print(a, b, z, sep=f' опа! ')
# print(a, b, z, sep=f'{age}')
# print(a, b, z, sep=str(age))
# print(a, b, z, sep='\n')
# print(a, b, z, sep='\t')

print(b, end=z)
print(a, end='~~~!!!~~~')

####################################

name = "John"
age = 25
print('Привет, меня зовут %s.' % name)
print('Привет, меня зовут {}, мне {} лет.'.format(name, age))
print('Привет, меня зовут {b}, мне {a} лет.'.format(a=name, b=age))
print(f'Привет, меня зовут {name}, мне {age} лет.')

####################################

s= 'Python !'
print(*s) # -> print('P', 'y', 't', 'h', 'o', 'n', ' ', '!')
print()
print(*s, sep='\n')

# выведет:

# P y t h o n

# P
# y
# t
# h
# o
# n



