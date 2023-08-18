from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort(reverse=True)
ans, base, limit = 0, 0, 0

tf = [1 for _ in range(n * 2)]

while base < n * 2:
    limit = arr[base % n]

    if limit != 0:
        while limit > 0:
            if tf[base]:
                ans += 1

            tf[base] = 0
            tf[(base + n) % (n * 2)] = 0
            limit -= 1
            base += 1

    else:
        tf[base] = 0
        tf[(base + n) % (n * 2)] = 0
        base += 1

print(ans)