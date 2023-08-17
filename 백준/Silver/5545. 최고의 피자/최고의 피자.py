from sys import stdin

n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
kal_d = int(stdin.readline())

d = []
for _ in range(n):
    d.append(int(stdin.readline()))

d.sort(reverse=True)
answer = kal_d // a
cnt = 0

for i in range(1, len(d) + 1):
    cal = kal_d + sum(d[0:i])
    price = a + b * i

    if cal / price > answer:
        answer = cal / price
    else:
        break

print(int(answer))
