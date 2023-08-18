from sys import stdin

ans = 0
for i in range(int(stdin.readline())):
    k = int(stdin.readline())
    if i == 0:
        ans = k
        continue
    if ans < k:
        print('N')
        exit()

print('S')