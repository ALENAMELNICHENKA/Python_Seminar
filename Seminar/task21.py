# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#          {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'} 
# Примечание: Список словарей задан изначально. Пользователь его не вводит.

list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
             {"VII": "S005"}, {" V ":"S009"}, {"VIII":"S007"}]

unique = set()

for cur_dict in list_dict:
    for value in cur_dict.values():
        unique.add(value)
print(unique)

#2 Решение. Применимо с одним элементом в словаре:

# for cur_dict in list_dict:
#         unique.add(*cur_dict.values())
# print(unique)

#3 Решение. Метод update, кот. распаковывает все элементы в словаре:

unique = set()
for cur_dict in list_dict:
         unique.update(cur_dict.values())
print(unique)
