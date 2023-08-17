from sys import stdin
a, b = map(int, stdin.readline().split())
ans = str(a // b) + '.'
a = a % b

for _ in range(100):
    ans += str((a * 10) // b)
    a = (a * 10) % b

print(ans)