import re
p = re.compile('[_0-9a-zA-Z]+[_\.0-9a-zA-Z]*@[0-9a-zA-Z_]+[\.0-9a-zA-Z_]+[0-9a-zA-Z_]+')
n = int(input())
l = []
for i in range(n):
    x = str(input())
    r = re.findall(p, x)
    for z in r:
        if(z not in l):
            l.append(z)
l.sort()
for i in range(len(l)):
    if(i == len(l)-1):
        print(l[i])
    else:
        print(l[i],end=";")
