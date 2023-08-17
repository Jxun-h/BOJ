from sys import stdin

n = int(stdin.readline())

for i in range(1, n + 1):
    temp = sum(map(int, list(str(i)))) + i
    if n == temp:
        print(i)
        exit()
print(0)
