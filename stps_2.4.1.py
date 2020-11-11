'''
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
'''
myList = []
with open('/Users/mk/Documents/temp/dataset_24465_4.txt', 'r') as str0:  # open the file from Mac
    for i in str0:
        myList.append(i)
str0.close()  # close the file
myList.reverse()

with open('/Users/mk/Documents/temp/resultR.txt', 'w') as str1:  # open the file from Mac
    for i in myList:
        str1.write(i)
str1.close()
