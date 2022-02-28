def convert_base(num, from_base, to_base):
    n = int(num, from_base) if isinstance(num, str) else num
    alph = '0123456789' + ''.join([chr(i + 65) for i in range(26)]) + ''.join([chr(i + 97) for i in range(26)])
    print(alph)
    res = ''
    while n > 0:
        n, m = divmod(n, to_base)
        res += alph[m]
    return res[::-1]


print(convert_base('0b010010001110010', 2, 8))
