def go(n):
    return n >= 25


def petya_win(n):
    return go(n + 1) and go(n * 2)


def vanya_win(n):
    return petya_win(n + 1) or petya_win(n * 2) and not (petya_win(n))


def petya_win2(n):
    return (vanya_win(n + 1) and vanya_win(n * 2)) and not (vanya_win(n))


def vanya_win2(n):
    return (petya_win2(n + 1) or petya_win2(n * 2)) and not (petya_win2(n))


for i in range(1, 24):
    if vanya_win2(i):
        print(i)