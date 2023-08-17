from sys import stdin

a, b= map(int, stdin.readline().split())
ans = []
for i in range(min(a, b) + 1, max(a, b)):
    ans.append(i)

print(len(ans))
print(*ans)