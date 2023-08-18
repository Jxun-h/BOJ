from sys import stdin

n, m = map(int, stdin.readline().split())
bits = [0 for _ in range(n)]
visited = set()

for _ in range(m):
    data = list(map(int, stdin.readline().rstrip().split()))

    if len(data) == 3:
        c, i, x = data

        if c == 1:
            temp = 1 << (x - 1)
            bits[i - 1] = temp | bits[i - 1]

        else:
            temp = 1 << 20
            temp -= 1
            temp -= (1 << x - 1)

            bits[i - 1] = temp & bits[i - 1]


    else:
        c, i = data

        if c == 3:
            bits[i - 1] = bits[i - 1] << 1
            temp = 1 << 20
            temp -= 1

            bits[i - 1] = temp & bits[i - 1]

        else:
            bits[i - 1] = bits[i - 1] >> 1


ans = 0
for i in bits:
    if i not in visited:
        visited.add(i)
        ans += 1

print(ans)