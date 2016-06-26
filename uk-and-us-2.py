import re
sent = []
n = int(input())
for i in range(n):
    x = str(input())
    sent.append(x)
t = int(input())
for i in range(t):
    x = str(input())
    y = x
    c = 0
    x = x.replace('our','or')
    p = re.compile('(?:\s|\A)'+'('+x+'|'+y+')'+'(?=\s|\Z)')
    for sen in sent:
        c += len(re.findall(p, sen))
    print(c)
