from sys import stdin
from itertools import combinations

start_end = {}
s = list(stdin.readline().rstrip())
pre = []
for i in range(len(s)):
    if s[i] == '(':
        pre.append(i)

    elif s[i] == ')':
        if pre:
            start_end[pre.pop()] = i


g = []

for start, end in sorted(start_end.items()):
    g.append((start, end))


ans = set()

for i in range(1, len(g) + 1):
    for comb in list(set(combinations(g, i))):
        temp = s[:]
        for st, end in comb:
            temp[st] = ''
            temp[end] = ''
            ans.add(''.join(temp))

print(*sorted(ans), sep='\n')