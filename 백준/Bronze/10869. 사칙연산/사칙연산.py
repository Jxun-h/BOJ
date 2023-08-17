from sys import stdin

a, b = map(int, stdin.readline().split())
ans = [a + b, a - b, a * b, a // b, a % b]
for i in ans:
    print(i)
