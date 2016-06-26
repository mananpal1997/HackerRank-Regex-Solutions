import sys
x = sys.stdin.read()
x = str(x)
if('String args[]' in x or 'java.' in x or 'IOException' in x):
    print("Java")
elif('#include' in x or 'return 0' in x or 'void main(' in x or 'int main(' in x):
    print("C")
else:
    print("Python")
