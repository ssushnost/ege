def convert_base(num, from_base=10, to_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alph = '0123456789' + ''.join([chr(i + 65) for i in range(26)]) + ''.join([chr(i + 97) for i in range(26)])
    ans = ''
    while n > 0:
        ans += alph[n % to_base]
        n //= to_base
    return ans[::-1]


for i in range(2,1000): # обязательно начинать с 2
    if convert_base(18,to_base=i) == '30':
        print(i)
        break

