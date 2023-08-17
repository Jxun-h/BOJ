from sys import stdin

for _ in range(int(stdin.readline())):
    ans = ''
    a, b = stdin.readline().rstrip().split()
    a = int(a)
    for i in b:
        ans += i * a
    print(ans)