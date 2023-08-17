from sys import stdin


for tc in range(int(stdin.readline())):
    k, n = map(int, stdin.readline().split())
    arr = [list(map(int, stdin.readline().split())) for _ in range(4)]
    f, s = [], []
    for i in range(n):
        for j in range(n):
            data = arr[0][i] + arr[1][j]
            f.append(data)

    for i in range(n):
        for j in range(n):
            data = arr[2][i] + arr[3][j]
            s.append(data)

    f.sort()
    s.sort()
    l, r = 0, len(s) - 1
    ans, diff = int(1e9), int(1e9)

    while l < len(f) and r >= 0:
        temp_diff = abs(f[l] + s[r] - k)
        if temp_diff < diff:
            diff = temp_diff
            ans = f[l] + s[r]

        elif temp_diff == diff:
            ans = min(ans, f[l] + s[r])

        if f[l] + s[r] > k:
            r -= 1

        elif f[l] + s[r] < k:
            l += 1

        else:
            break

    if l < len(f) and r >= 0:
        temp_diff = abs(f[l] + s[r] - k)
        if temp_diff < diff:
            diff = abs(f[l] - s[r] - k)
            ans = f[l] + s[r]

    print(ans)