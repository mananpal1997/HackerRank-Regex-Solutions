import re
p = re.compile('^\d+\s+(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$')
n = int(input())
for i in range(n):
    x = str(input())
    if(len(re.findall(p, x)) > 0):
        print("VALID")
    else:
        print("INVALID")
