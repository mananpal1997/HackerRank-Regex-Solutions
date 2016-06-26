import re
p = re.compile('[A-Z]{5}[0-9]{4}[A-Z]')
n = int(input())
for i in range(n):
    x = str(input())
    if(len(x) != 10):
        print("NO")
    elif(len(re.findall(p, x)) > 0):
        print("YES")
    else:
        print("NO")
