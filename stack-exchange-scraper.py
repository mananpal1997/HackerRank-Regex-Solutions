import re, sys
p1 = re.compile('<a href="/questions/([0-9]+).*>')
p2 = re.compile('<a href="/questions/[0-9]+.*>(.*)</a>')
p3 = re.compile('.*class="relativetime">(.*)</span>')
a = sys.stdin.read()
x = re.findall(p1, a)
y = re.findall(p2, a)
z = re.findall(p3, a)
for i in range(len(x)):
    print(x[i].strip()+';'+y[i].strip()+';'+z[i].strip())
