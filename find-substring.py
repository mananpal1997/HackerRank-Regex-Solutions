import re
n = int(input())
x = []
for i in range(n):
    y = str(input())
    x.append(y)
t = int(input())
for i in range(t):
    y = str(input())
    pattern = re.compile('\w+'+y+'\w+')
    count = 0
    for z in x:
        count += len(re.findall(pattern, z))
    print(count)
