from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().rstrip()
check = 'I'
for i in range(n):
    check += 'OI'


def solve(i):
    if s[i:i+len(check)] == check:
        return True
    return False


cnt = 0
for i in range(m):
    if s[i] == 'I':
        if solve(i):
            cnt += 1

print(cnt)