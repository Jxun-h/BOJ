from sys import stdin

n, b = map(int, stdin.readline().split())
block = list(map(int, stdin.readline().split()))
answer = 0

if b == 1:
    answer += n
    for i in range(n - 3):
        if block[i] == block[i + 1] == block[i + 2] == block[i + 3]:
            answer += 1

elif b == 2:
    for i in range(n - 1):
        if block[i] == block[i + 1]:
            answer += 1

elif b == 3:
    for i in range(n - 2):
        if block[i] == block[i + 1] == block[i + 2] - 1:
            answer += 1

    for i in range(n - 1):
        if block[i] - 1 == block[i + 1]:
            answer += 1
    
elif b == 4:
    for i in range(n - 2):
        if block[i] - 1 == block[i + 1] == block[i + 2]:
            answer += 1

    for i in range(n - 1):
        if block[i] == block[i + 1] - 1:
            answer += 1

elif b == 5:
    for i in range(n - 2):
        if block[i] == block[i + 1] == block[i + 2]:
            answer += 1

        if block[i] == block[i + 1] + 1 == block[i + 2]:
            answer += 1

    for i in range(n - 1):
        if block[i] == block[i + 1] - 1:
            answer += 1

        if block[i] - 1 == block[i + 1]:
            answer += 1

elif b == 6:
    for i in range(n - 2):
        if block[i] == block[i + 1] == block[i + 2]:
            answer += 1

        if block[i] + 1 == block[i + 1] == block[i + 2]:
            answer += 1

    for i in range(n - 1):
        if block[i] == block[i + 1]:
            answer += 1

        if block[i] == block[i + 1] + 2:
            answer += 1

elif b == 7:
    for i in range(n - 2):
        if block[i] == block[i + 1] == block[i + 2]:
            answer += 1

        if block[i] == block[i + 1] == block[i + 2] + 1:
            answer += 1

    for i in range(n - 1):
        if block[i] == block[i + 1]:
            answer += 1

        if block[i] + 2 == block[i + 1]:
            answer += 1

print(answer)