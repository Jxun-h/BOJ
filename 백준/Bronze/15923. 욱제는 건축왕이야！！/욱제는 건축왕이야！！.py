from sys import stdin

n = int(stdin.readline().rstrip())
x, y = map(int, stdin.readline().rstrip().split())
sx, sy = x, y
result = 0

for step in range(1, n):
    a, b = map(int, stdin.readline().rstrip().split())

    result += abs(x + y - a - b)
    x, y = a, b

result += abs(x + y - sx - sy)

print(result)