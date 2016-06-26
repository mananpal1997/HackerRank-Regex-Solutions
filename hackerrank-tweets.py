import re
p = re.compile('((h|H)(a|A)(c|C)(k|K)(e|E)(r|R)(r|R)(a|A)(n|N)(k|K))')
t = int(input())
c = 0
for i in range(t):
    x = str(input())
    c += len(re.findall(p, x))
print(c)
