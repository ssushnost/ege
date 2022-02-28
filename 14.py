def convert_base(num, from_base=10, to_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alph = '0123456789' + ''.join([chr(i + 65) for i in range(26)]) + ''.join([chr(i + 97) for i in range(26)])
    ans = ''
    while n > 0:
        ans += alph[n % to_base]
        n //= to_base
    return ans[::-1]


cnt = 0
for i in range(10, 17 + 1):
    cnt += convert_base(i, to_base=5).count('2')
print(cnt)
