import sys
n = int(sys.stdin.readline())
stack = list(map(int, sys.stdin.readline().split(" ")))
edge = [[-1] for _ in range(n)]
k = int(sys.stdin.readline())
root = []
for i in range(0,n):
    if stack[i] >= 0 and i != k:
        edge[stack[i]].append(i)
    elif stack[i] == -1 and i != k:
        root.append(i)
edge[k] = [-1]
ans = 0

visited = [0]*n
while root:
    n = root.pop()
    if visited[n] == 0:
        visited[n] = 1
        if len(edge[n]) == 1:
            ans += 1
        else:
            sub = edge[n]
            sub.pop(0)
            for i in sub:
                root.append(i)
print(ans)