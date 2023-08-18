from sys import stdin

a, b = map(int, stdin.readline().split())
mod, pos = a, 0
arr = [i for i in range(1, a + 1)]
res = []

while arr:
    idx = (pos + (b - 1)) % mod
    res.append(str(arr.pop(idx)))
    pos = idx
    mod = len(arr)

ans = ', '.join(res)
print('<'+ans+'>')
