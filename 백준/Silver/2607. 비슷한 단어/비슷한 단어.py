from sys import stdin

n = int(stdin.readline())
inp = []
word = []
for i in range(n):
    inp.append(stdin.readline().rstrip())

word = [sorted(list(inp[i])) for i in range(n)]
find = [len(inp[i]) if len(inp[i]) >= len(word[0]) else len(word[0]) for i in range(n)]

for i in range(1, n):
    for j in range(len(word[0])):
        for k in range(len(word[i])):
            if word[i][k] == word[0][j]:
                find[i] -= 1
                word[i][k] = ' '
                break

cnt = 0
for i in range(1, n):
    if find[i] <= 1:
        cnt += 1
print(cnt)