import re
pattern = re.compile('^[_\.][0-9]+[a-zA-Z]*[_]?$')
n = int(input())
for i in range(n):
    x = str(input())
    if(len(re.findall(pattern,x)) != 0):
        print("VALID")
    else:
        print("INVALID")
