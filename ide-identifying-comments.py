import re, sys
l = []
x = sys.stdin.read()
x = str(x)
for i in range(len(x)):
    if(x[i] == '\n'):
        x = x[:i] + '$$' + x[i+1:]
        while(i < len(x) and x[i+1] == '\n'):
            i += 1
            x = x[:i] + x[i+1:]
x += '$$'
p1 = re.compile('(//[^$]*[$]*)|(/\*[\d\D]*?\*/)')
l = []
if(len(re.findall(p1, x)) != 0):
    for z in re.findall(p1, x):
        l.append(z)
zzz = []
for y in l:
    for z in y:
        if(len(z) != 0):
            z = z.replace('$$','\n')
            z = z.strip()
            bb = z.split('\n')
            for qq in bb:
                zzz.append(qq)
for p in zzz:
    print(p.strip())
