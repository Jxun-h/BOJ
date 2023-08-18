from sys import stdin

n, m = map(int, stdin.readline().split())
needs = list(map(int, stdin.readline().split()))
ans = 0


def check(num):
    for v in needs:
        if str(v) not in num:
            return False
    return True


for i in range(10 ** n):
    if check('0' * (n - len(str(i))) + str(i)):
        ans += 1

print(ans)