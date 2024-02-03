# Задача №27.
# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте. 
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells 
# Output: 13

my_string = "She sells sea shells on the sea shore The shells that she sells are sea shells "\
"I'm sure So if she sells sea shells on the sea shore. I'm sure that the shells are sea shore shells"
 

# Приведём к одному регистру и избавимся от точки в тексте .replace('.', '')
my_string = my_string.upper().replace('.', '')
print(my_string)
# Строку преобразуем в список и разделяем в слова
my_list = my_string.split()
#Находим количество уникальных слов и выводим
print(len(set(my_list)))

#Можно записать в одну строку:
print(len(set(my_string.upper().replace('.', '').split())))