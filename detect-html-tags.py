import re
pattern = re.compile('<\\s*([a-zA-Z0-9]*)\\s*>?')
n = int(input())
tag_list = list()
for i in range(n):
    x = str(input())
    y = re.findall(pattern, x)
    for z in y:
        if(len(z) != 0 and z not in tag_list):
            tag_list.append(z)
tag_list.sort()
for i in range(len(tag_list)):
    if(i == len(tag_list) - 1):
        print(tag_list[i])
    else:
        print(tag_list[i],end=";")
