'''
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.
В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов
наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс
не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
В следующей строке содержится число q - количество запросов.
В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No",
если не является.

Sample Input:
5
A
B : A
C : A
D : B C
F : B A
6
A B
B C
A C
A D
A F
F F

При вводе - B : A = B(A) B наследуется от А
При выводе - A B = наследуется ли B от А? (т.е. является ли А предком В?)

Sample Output:
Yes
Yes
Yes
No
'''


# use this function for searching the path between start and end
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


# first part of input here
myClasses = {}
myList = []
tempList = []
numbClasses = int(input())
for i in range(numbClasses):
    myList.append(input().split())
    for l in myList[i][2:]:
        tempList.append(l)
        if not (myClasses.get(l) == None):
            tempList.extend(myClasses.get(myList[i][2]))
    myClasses.update({myList[i][0]: tempList})
    tempList = []

# second part of input and calling the function
myList2 = []
numbCheks = int(input())
for i in range(numbCheks):
    myList2.append(input().split())

for i in myList2:
    if find_path(myClasses, i[1], i[0]) == None:
        print("No")
    else:
        print("Yes")
