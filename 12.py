string = '8'*68
while '222' in string or '888' in string:
    if '222' in string:
        string = string.replace('222','8',1)
    else:
        string = string.replace('888','2',1)
print(string)