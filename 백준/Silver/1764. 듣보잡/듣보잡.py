from sys import stdin

n, m = map(int, stdin.readline().split())
d_set, b_set = set(), set()

for _ in range(n):
    d = stdin.readline().rstrip()
    d_set.add(d)

for _ in range(m):
    b = stdin.readline().rstrip()
    b_set. add(b)

temp1 = d_set - b_set
temp2 = b_set - d_set

ans = set()
ans.update(d_set)
ans.update(b_set)
ans = (ans - temp1) - temp2

print(len(ans), *sorted(list(ans)), sep='\n')