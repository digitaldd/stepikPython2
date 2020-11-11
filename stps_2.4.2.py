'''
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
'''
import os.path

os.chdir('/Users/mk/Documents/temp/')
answer = []
for path, dirs, files in os.walk('.'):
    for name in files:
        if (name.endswith(".py")) & (not answer.__contains__(path)):
            answer.append(path)

answer.sort()
with open('/Users/mk/Documents/temp/resultR.txt', 'w') as str1:  # open the file from Mac
    for i in answer:
        str1.write(i[2:] + "\n")
str1.close()
