from sys import stdin

n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
state = [0 for _ in range(n)]
cnt = 0

for i in range(n):
    if base[i] != state[i]:
        for j in range(3):
            if i + j >= n:
                break
            else:
                state[i + j] = 1 if state[i + j] == 0 else 0
        cnt += 1

print(cnt)
