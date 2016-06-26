import re
n = int(input())
l = []
for i in range(n):
    x = str(input())
    l.append(x)
pattern = re.compile('<a href="(.+?)".*?>(.*?)<\/a>')
for x in l:
        a = re.findall(pattern, x)
        for z in a:
            y1 = z[0].strip()
            y2 = z[1].strip()
            p2 = re.compile('[<.*>]*(.*?)<.*>')
            y2 = re.findall(p2, y2)
            if(len(y2) != 0):
                y2 = str(y2)
                y2 = y2[2:len(y2)-2]
                zz = y2.find('>')
                y2 = y2[zz+1 : len(y2)]
                print(y1+','+y2)
            else:
                print(y1 + ',' + z[1].strip())
