from sys import stdin

n, k = map(int, stdin.readline().split())


def solve(n, k):
    s = list('B' * n)
    acnt, curk, lidx = 0, 0, -1

    while curk < k:
        if lidx <= acnt - 1:
            if s[n - 1 - (acnt + 1)] == 'A':
                break

            s[n - 1 - (acnt + 1)] = 'A'
            lidx = n - 1 - (acnt + 1)
            acnt += 1
            curk += 1
        else:
            s[lidx] = 'B'
            s[lidx - 1] = 'A'
            lidx -= 1
            curk += 1

    return s if curk == k else '-1'


answer = solve(n, k)
print(*answer, sep='')