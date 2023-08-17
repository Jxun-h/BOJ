from sys import stdin

for _ in range(int(stdin.readline())):
    ans = 0
    for i in range(1, int(stdin.readline()) + 1):
        if i % 2 != 0:
            ans += i
    print(ans)