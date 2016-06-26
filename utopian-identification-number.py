import re
p = re.compile('^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}')
n = int(input())
for i in range(n):
    x = str(input())
    if(len(re.findall(p, x)) > 0):
        print("VALID")
    else:
        print("INVALID")
