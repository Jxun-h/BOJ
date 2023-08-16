import re
from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().rstrip()
    patterns = '(100+1+|01)+'
    res = re.fullmatch(patterns, s)
    print('YES' if res is not None else 'NO')