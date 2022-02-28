def f(n, end, not_include):
    if n == end:
        return 1
    if n > end or n == not_include:
        return 0
    return f(n + 1, end, not_include) + f(n + 2, end, not_include) + f(n * 2, end, not_include)


print(f(3, 10, -1)*f(10,12,-1))
