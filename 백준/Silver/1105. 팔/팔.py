from sys import stdin

l, r = stdin.readline().rstrip().split()
ans = 0

if len(l) != len(r):
    print(0)
else:
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                ans += 1
        else:
            break

    print(ans)