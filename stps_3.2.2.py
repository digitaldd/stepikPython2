'''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa

Sample Input 1:
abababa
aba
Sample Output 1:
3
'''

s, t = [input("") for x in range(2)]
count, index = 0, 0
while True:
    index = s.find(t, index)
    if index != -1:
        count += 1
        index += 1
    else:
        break
print(count)