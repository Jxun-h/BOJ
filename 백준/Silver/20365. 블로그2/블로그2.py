from sys import stdin

ans = [1, 1]
n = int(stdin.readline())
s = list(stdin.readline().rstrip()) + ['A']

for i in range(n):
    if s[i] != 'B':
        ans[0] += 1
        if s[i + 1] == 'R':
            ans[0] -= 1


for i in range(n):
    if s[i] != 'R':
        ans[1] += 1
        if s[i + 1] == 'B':
            ans[1] -= 1


print(min(ans))
