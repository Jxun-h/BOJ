from sys import stdin

for i in list(stdin.readline().rstrip()):
    if i == ' ':
        print(' ', end='')
    elif i.isnumeric():
        print(i, end='')
    else:
        if i.isupper():
            temp = ord(i) + 13
            if temp > 90:
                print(chr(temp - 26), end='')
            else:
                print(chr(temp), end='')
        else:
            temp = ord(i) + 13
            if temp > 122:
                print(chr(temp - 26), end='')
            else:
                print(chr(temp), end='')