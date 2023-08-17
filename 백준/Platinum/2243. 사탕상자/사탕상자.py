import sys

input = sys.stdin.readline

def init(n, s, e, t, v):
    if t < s or e < t:
        return tree[n]
    
    if s == t == e:
        tree[n] += v
        arr[n] = t
        return tree[n]
    
    m = (s + e) // 2
    tree[n] = init(n * 2, s, m, t, v) + init(n * 2 + 1, m + 1, e, t, v)

    return tree[n]

def get(n, s, e, g):
    if (s == e):
        tree[n] -= 1
        print(arr[n])
        return tree[n]

    l = tree[n * 2]
    m = (s + e) // 2
    if l >= g:
        get(n * 2, s, m, g)
    else:
        get(n * 2 + 1, m + 1, e, g - tree[n * 2])

    tree[n] = tree[n * 2] + tree[n * 2 + 1]

    return tree[n]

N = int(input())
tree = [0] * (1000000 * 4)
arr = [0] * (1000000 * 4)

for _ in range(N):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        get(1, 1, 1000000, cmd[1])
    elif cmd[0] == 2:
        init(1, 1, 1000000, cmd[1], cmd[2])