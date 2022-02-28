def go(n):
    return n >= 25


def petya_win(n):
    return go(n + 1) or go(n * 2)


def vanya_win(n):
    return petya_win(n + 1) and petya_win(n * 2) and not (petya_win(n))


def petya_win2(n):
    return (vanya_win(n + 1) or vanya_win(n * 2)) and not (vanya_win(n))


for i in range(1, 24):
    if petya_win2(i):
        print(i)
