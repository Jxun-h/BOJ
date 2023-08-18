from sys import stdin

ans = int(1e9)

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    if a <= b:
        ans = min(ans, b)

print(ans if ans != int(1e9) else -1)