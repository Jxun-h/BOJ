from sys import stdin
n, k = map(int, stdin.readline().split())
temp = list(map(int, stdin.readline().split()))
answer = 0
temp.sort()

i = 0
for j in range(n):
    answer += temp[j] * i
    if i < k:
        i += 1

print(answer)