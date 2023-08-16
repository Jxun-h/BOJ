from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
plus, minus, count = [], [], []

for k in arr:
    plus.append(k) if k > 0 else minus.append(abs(k))

plus.sort()
minus.sort()

cnt = 0
while plus:
    if cnt == m:
        cnt = 0

    data = plus.pop()
    if cnt == 0:
        count.append(data)
    cnt += 1

cnt = 0
while minus:
    if cnt == m:
        cnt = 0

    data = minus.pop()
    if cnt == 0:
        count.append(data)
    cnt += 1

count.sort()

answer = count.pop()
answer += sum(count) * 2

print(answer)