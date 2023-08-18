from sys import stdin

n = int(stdin.readline())

binary_n = bin(n)[2:]
binary_m = ''

for i in binary_n:
    if binary_m == '' and i == '1':
        pass

    elif i == '0':
        binary_m += '1'

    else:
        binary_m += '0'

if binary_m == '':
    print(1)
    print(int(binary_n, 2))
else:
    print(2)
    for i in sorted([int(binary_n, 2), int(binary_m, 2)]):
        print(i)
