from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
stack = []
ans = [0 for _ in range(n)]


for i in range(n):
    while stack:
        if stack[-1][1] > data[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append((i, data[i]))

print(*ans)