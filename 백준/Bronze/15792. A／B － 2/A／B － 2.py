from sys import stdin
a, b = map(int, stdin.readline().split())
ans = '' + str(a // b) + '.'
a %= b
a *= 10

for _ in range(1000):
    temp = a // b
    ans += str(temp)
    a %= b
    a *= 10

print(ans)