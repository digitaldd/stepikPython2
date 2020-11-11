'''
Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...
Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде
будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого
положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.

Важное примечание:
В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее
где-то поймали их предка.

Формат входных данных

В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных

Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом
поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

Пример теста 1

Рассмотрим код

try:
   foo()
except ZeroDivision :
   print("ZeroDivision")
except OSError:
   print("OSError")
except ArithmeticError:
   print("ArithmeticError")
except FileNotFoundError:
   print("FileNotFoundError")
...

По условию этого теста, Костя посмотрел на этот код, и сказал Антону, что исключение
FileNotFoundError можно не ловить, ведь мы уже ловим OSError -- предок FileNotFoundError

Sample Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:
FileNotFoundError
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

# second part of input
myList2 = []
numbCheks = int(input())
for i in range(numbCheks):
    myList2.extend(input().split())

# calling the function and output
checkList = []
resultList = []
count = 0
for i in myList2:
    count += 1
    checkList = myList2[:count]
    for k in checkList:
        if find_path(myClasses, str(i), str(k)) == None:
            continue
        elif len(find_path(myClasses, str(i), str(k))) > 1:
            if not (resultList.__contains__(i)):
                resultList.append(i)
for i in resultList: print(i)
