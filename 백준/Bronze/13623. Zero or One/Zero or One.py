from sys import stdin

data = stdin.readline().rstrip().replace(' ', '')
if data == '100' or data == '011':
    print('A')
elif data == '010' or data == '101':
    print('B')
elif data == '001' or data == '110':
    print('C')
else:
    print('*')