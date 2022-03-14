def go(a,b):
    return a+b>=58

def p1(a,b):
    return go(a+1,b) or go(a,b+1) or go(a+b,b) or go(a,a+b)

def p1l(a,b):
    return go(a+1,b) or go(a,b+1) or go(a+b,b) or go(a,a+b)

def v1(a,b):
    return p1(a+1,b) and p1(a,b+1) and p1(a+b,b) and p1(a,a+b) and not p1l(a,b)

def v1l(a,b):
    return p1(a+1,b) or p1(a,b+1) or p1(a+b,b) or p1(a,a+b)

def p2(a,b):
    return v1(a+1,b) or v1(a,b+1) or v1(a+b,b) or v1(a,a+b)

for i in range(1,51+1):
    if p2(6,i):
        print(i)
