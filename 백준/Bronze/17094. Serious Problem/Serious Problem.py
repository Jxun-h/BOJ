from sys import stdin

n = int(stdin.readline())
l = stdin.readline().rstrip().count('e')
if (n-l) > l:
    print(2)
elif (n-l) < l:
    print('e')
else:
    print('yee')
