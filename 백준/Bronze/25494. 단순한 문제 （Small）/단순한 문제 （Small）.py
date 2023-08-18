from sys import stdin

for tc in range(int(stdin.readline())):
    a, b, c = map(int, stdin.readline().split())

    ans = 0

    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                if x % y == y % z == z % x:
                    ans += 1

    print(ans)