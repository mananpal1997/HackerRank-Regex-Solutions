import re
p = re.compile('<[a-zA-Z0-9]+\s*[^>]*>')
n = int(input())
tags = []
attr = dict()
for i in range(n):
    x = str(input())
    y = re.findall(p, x)
    if(len(y) > 0):
        for z in y:
            p1 = re.compile('<([a-zA-Z0-9]+)\s*(.*)>')
            p2 = re.compile('(\S+)=["\'][^\'"]*["\']?')
            c = re.findall(p1, z)
            c = c[0]
            c = list(c)
            for j in range(len(c)):
                if(len(c[j]) == 0):
                    c.remove(c[j])
            if(len(c) == 1):
                if(c[0] not in tags):
                    tags.append(c[0])
                    attr.update({c[0] : []})
            else:
                if(c[0] not in tags):
                    tags.append(c[0])
                    attr.update({c[0] : []})
                for z in re.findall(p2, c[1]):
                    li = attr[c[0]]
                    if(z not in li):
                        li.append(z)
                    attr.update({c[0] : li})
tags.sort()
for i in range(len(tags)):
    temp = attr[tags[i]]
    temp.sort()
    print(tags[i]+':',end='')
    for j in range(len(temp)):
        print(temp[j],end='')
        if(j != len(temp)-1):
            print(',',end='')
    print()
