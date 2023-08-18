from sys import stdin

n = int(stdin.readline())
s = stdin.readline().rstrip()
ans = 0
cnt, flag = 0, 0

for i in range(len(s)):
    if s[i] == 'X':
        cnt = 0
    else:
        if flag:
            cnt += 1
            ans += (i + 1) + cnt
            continue

        ans += (i + 1) + cnt
        cnt += 1
print(ans)