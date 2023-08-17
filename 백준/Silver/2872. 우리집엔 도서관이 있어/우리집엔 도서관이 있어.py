from sys import stdin


books = [int(stdin.readline().rstrip()) for _ in range(int(stdin.readline().rstrip()))]
max = books[0]
cnt = 0
for i in books[1:]:
    if i > max:
        if max + 1 != i:
            cnt += 1
        max = i
    else:
        cnt += 1
print(cnt)