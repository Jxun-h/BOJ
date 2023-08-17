from sys import stdin

s = list(stdin.readline().rstrip())
stack, d = [], {}
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)

    elif s[i] == ')':
        key = stack.pop()
        d[key] = i


def solve(l, r):
    res = 0
    idx = l
    while idx < r:
        if idx + 1 == r and s[idx].isalnum():
            res += 1
            idx += 1

        elif s[idx + 1] == '(':
            res += int(s[idx]) * solve(idx + 2, d[idx + 1])
            idx = d[idx + 1] + 1

        elif s[idx + 1].isalnum() or s[idx + 1] == ')':
            res += 1
            idx += 1

    return res


print(solve(0, len(s))) if d else print(len(s))
