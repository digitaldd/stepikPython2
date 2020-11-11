'''
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле
name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно
от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:
A : 3
B : 1
C : 2
'''

# task 1.6.1 maybe 2.1.2

import json


# find a path between start and end
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if graph.get(start) == None:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


# just check all elements from dictionary through the find_path
def startSearching(parent):
    answer = []
    for key in myDict1.keys():
        for x in myDict1.get(key):
            if not find_path(myDict1, x, parent) is None:
                answer.extend(set(find_path(myDict1, x, parent)))
            if not find_path(myDict1, key, parent) is None:
                answer.extend(find_path(myDict1, key, parent))
    return answer


# get data from input in json and create a dictionary from it
myDict1 = {}
js = json.loads(input(""))
for j in js:
    myDict1.update({dict(j).get("name"): set(dict(j).get("parents"))})
keys = list(myDict1.keys())
keys.sort()
for key in keys:
    print(key, ":", 1 if len(set(stratSearching(key))) == 0 else len(set(stratSearching(key))))
