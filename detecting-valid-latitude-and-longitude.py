import re
p = re.compile('([+-]*\d*[\.]*\d*), ([+-]*\d*[\.]*\d*)')
t = int(input())
for i in range(t):
    try:
        z = str(input())
        z = z[1:len(z)-1]
        zz = re.findall(p, z)
        zz = zz[0]
        x = zz[0]
        y = zz[1]
        if(x[0] == '+' or x[0] == '-'):
            x = x[1:]
        if(y[0] == '+' or y[0] == '-'):
            y = y[1:]
        if(x[len(x)-1] == '.' or y[len(y)-1] == '.'):
            print("Invalid")
            continue
        if((len(x) > 1 and x[0] == '0' and x[1] != '.') or (len(y) > 1 and y[0] == '0' and y[1] != '.')):
            print("Invalid")
            continue
        x = float(x)
        y = float(y)
        if(x >= -90.0 and x <= 90.0 and y >= -180.0 and y <= 180.0):
            print("Valid")
        else:
            print("Invalid")
    except:
        print("Invalid")
