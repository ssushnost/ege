def go(n):
    return n >= 25


def petya_win(n):
    return go(n + 1) or go(n * 2)


def vanya_win(n):
    return petya_win(n + 1) and petya_win(n * 2) and not (petya_win(n))


for i in range(1, 24):
    if vanya_win(i):
        print(i)
