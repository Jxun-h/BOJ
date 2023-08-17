from sys import stdin

res = 1
for i in range(3):
    res *= int(stdin.readline())

ans = [0 for i in range(10)]
for i in str(res):
    ans[int(i)] += 1

print(*ans, sep='\n')