from sys import stdin

flag=0
k = int(stdin.readline())
for _ in range(k):
    n = stdin.readline().rstrip()
    if n == 'anj':
        flag = 1
        break

if flag:
    print('뭐야;')
else:
    print('뭐야?')