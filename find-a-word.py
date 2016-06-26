import re
n = int(input())
sen = list()
for i in range(n):
    x = str(input())
    sen.append(x)
t = int(input())
for i in range(t):
    x = str(input())
    p = re.compile('(?:\W|\A)'+x+'(?=\W|\Z)')
    c = 0
    for y in sen:
        c += len(re.findall(p, y))
    print(c)
