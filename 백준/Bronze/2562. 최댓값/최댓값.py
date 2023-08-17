from sys import stdin

idx, h = 0, 0
for i in range(9):
    n = int(stdin.readline())
    if n > h:
        idx = i + 1
        h = n
print(h)
print(idx)