from sys import stdin

while 1:
    s = stdin.readline().rstrip().lower()
    a = [0 for _ in range(26)]
    if s == '#':
        break
    for i in s:
        n = ord(i)
        if 97 <= n <= 122:
            if a[n - 97] == 0:
                a[n - 97] = 1

    print(sum(a))
