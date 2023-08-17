from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().rstrip()
    cnt, ans = 0, 0
    for i in s:
        if i == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)