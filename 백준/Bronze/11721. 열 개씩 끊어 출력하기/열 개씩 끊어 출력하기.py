from sys import stdin
s = stdin.readline().rstrip()
l, r = 0, 10

for i in range(len(s) // 10 + 1):
    print(s[l:r])
    l += 10
    r += 10