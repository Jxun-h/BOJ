from sys import stdin

while 1:
    n = stdin.readline().rstrip()
    if n == '0':
        break
    l = len(n)
    if l % 2 == 0:
        if n[:l // 2][::-1] == n[l//2:]:
            print('yes')
        else:
            print('no')

    else:
        if n[:l // 2][::-1] == n[l // 2 + 1:]:
            print('yes')
        else:
            print('no')