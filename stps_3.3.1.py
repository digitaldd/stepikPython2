'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line

Sample Input:
catcat
cat and cat
catac
cat
ccaatt
Sample Output:
catcat
cat and cat
'''

# it works, but i need to study regular expressions
'''
import sys

pattern = "cat"
founded = []
for line in sys.stdin:
    line = line.rstrip()
    if line.count(pattern) >= 2:
        founded.append(line)
for i in founded:
    print(i)
'''

# another works solution (with regular func)
import re
import sys

pattern = "cat"
founded = []
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 1:
        founded.append(line)

for i in founded:
    print(i)
