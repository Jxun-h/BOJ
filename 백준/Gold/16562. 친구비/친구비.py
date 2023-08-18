import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, sys.stdin.readline().split())
friends = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(n + 1)]

for _ in range(m):
    v, w = map(int, sys.stdin.readline().split())
    union_parent(parent, v, w)

answer = 0
visited = set()
for i in range(1, n + 1):
    if i not in visited:
        temp = [i]
        cost = friends[i - 1]
        for j in range(1, n + 1):
            if i != j:
                if find_parent(parent, i) == find_parent(parent, j):
                    temp.append(j)
                    cost = min(cost, friends[j - 1])
        visited.update(temp)
        answer += cost

if k >= answer:
    print(answer)
else:
    print("Oh no")