from sys import stdin

n = int(stdin.readline())
res = 0

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    res += a * b

print('Yes' if res == n else 'No')