from sys import stdin

ans = [int(1e9), 0]
n = int(stdin.readline())


def count_odd(s):
    res = 0
    for i in s:
        if int(i) % 2 == 1:
            res += 1
    return res


def solve(n, cnt):
    s = str(n)
    cnt += count_odd(s)

    if len(s) == 1:
        ans[0] = min(ans[0], cnt)
        ans[1] = max(ans[1], cnt)
        return

    if len(s) == 2:
        solve(n // 10 + n % 10, cnt)

    for i in range(1, len(s) - 1):
        for j in range(i + 1, len(s)):
            new_n = int(s[:i]) + int(s[i:j]) + int(s[j:])
            solve(new_n, cnt)


solve(n, 0)
print(*ans)
