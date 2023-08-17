from sys import stdin

n, d, k, c = map(int, stdin.readline().split())
sushi = []
for _ in range(n):
    sushi.append(int(stdin.readline()))

sushi *= 2
sushi_cnt = [0 for _ in range(1, d + 2)]
total = 0

""" 0번째부터 k - 1번 째까지 고려해서 먹을 수 있는 스시의 가짓수"""
for i in range(k):
    sushi_cnt[sushi[i]] += 1
    if sushi_cnt[sushi[i]] == 1:
        total += 1

answer = total if sushi_cnt[c] >= 1 else total + 1


""" 여기서 최대 가짓수"""
for l in range(1, n):
    sushi_cnt[sushi[l - 1]] -= 1
    if sushi_cnt[sushi[l - 1]] == 0:
        total -= 1

    sushi_cnt[sushi[l + k - 1]] += 1
    if sushi_cnt[sushi[l + k - 1]] == 1:
        total += 1

    if sushi_cnt[c] == 0:
        answer = max(total + 1, answer)
    else:
        answer = max(total, answer)

print(answer)