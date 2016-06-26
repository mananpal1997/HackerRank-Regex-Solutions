import re
p = re.compile('(\d{1,3})[-|\s](\d{1,3})[-|\s](\d{4,10})')
n = int(input())
for i in range(n):
    x = str(input())
    if(len(re.findall(p, x)) > 0):
        y = re.findall(p, x)[0]
        print("CountryCode="+y[0]+",LocalAreaCode="+y[1]+",Number="+y[2])
