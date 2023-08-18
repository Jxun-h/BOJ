from sys import stdin

n = int(stdin.readline())
a = []
b = list(map(int, stdin.readline().split()))[::-1]

for i in range(1, n + 1):
    if a:
        if a[-1] == i:
            a.pop()
            continue

    while b:
        if b[-1] != i:
            a.append(b.pop())

        else:
            b.pop()
            break

print("Nice" if len(a) < 1 else "Sad")