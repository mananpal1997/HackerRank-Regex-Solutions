sen = []
import re
n = int(input())
for i in range(n):
    x = str(input())
    sen.append(x)
t = int(input())
for i in range(t):
    x = str(input())
    x = x[:len(x)-2]
    c = 0
    p = re.compile(x+'(se|ze)')
    for j in sen:
        c += len(re.findall(p, j))
    print(c)
