moves_count = 4
end = 17
for i in range(2 ** moves_count):
    start = 1
    b = '0' * (moves_count - len(bin(i)[2:])) + bin(i)[2:]
    for move in b:
        if move == '0':
            start **= 2
        elif move == '1':
            start += 1
        if start == end:
            print(''.join([str(int(i) + 1) for i in b]))
