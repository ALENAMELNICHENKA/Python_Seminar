#1 
# import L3_modul_1
# print(L3_modul_1.max1(5, 9))

#2
# from L3_modul_1 import max1
# print(max1(5, 9))

#3 импортировать все функции из модуля - "*"
# from L3_modul_1 import *
# print(max1(10, 9))

#Изменим название нашего модуля программно для покороче :)

import L3_modul_1 as m1
print(m1.max1(10, 5))
