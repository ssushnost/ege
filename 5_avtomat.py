for i in range(100,1000):
    s = str(i)
    a = int(s[0])+int(s[1])
    b = int(s[1]) + int(s[2])
    ans = str(max(a,b))+str(min(a,b))
    if ans=='1412':
        print(i)
        break
