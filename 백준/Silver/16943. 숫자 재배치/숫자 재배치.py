from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


a, b = stdin.readline().rstrip().split()
a = sorted(list(a), reverse=True)
used = {}

for i in a:
    if i not in used:
        used[i] = 1
    else:
        used[i] += 1


def solve(cnt, s):
    if int(b) < int(s + '0' * (len(a) - len(s))):
        return

    if cnt == len(a):
        print(s)
        exit()

    for i in range(len(a)):
        if used[a[i]] > 0 and not (s == '' and a[i] == '0'):
            used[a[i]] -= 1
            solve(cnt + 1, s + a[i])
            used[a[i]] += 1


if solve(0, '') is None:
    print(-1)