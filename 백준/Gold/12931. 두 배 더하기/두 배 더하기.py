from sys import stdin

n = int(stdin.readline())
A = [0 for _ in range(n)]
B = list(map(int, stdin.readline().split()))
res = 0
bad = []

# 두 배
while A != B:
    cnt = 0
    chk = False
    temp = B[:]
    for j in range(n):
        if B[j] % 2 == 0:
            temp[j] //= 2
            cnt += 1
            continue

        bad.append(j)

    if cnt == n:
        chk = True

    if chk:
        B = temp
        res += 1
    else:
        for i in bad:
            B[i] -= 1
            res += 1
        bad = []
        chk = True

print(res)