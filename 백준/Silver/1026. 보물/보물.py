from sys import stdin

n = int(stdin.readline())
a = sorted(list(map(int, stdin.readline().split())))
b = sorted(list(map(int, stdin.readline().split())), reverse=True)
print(sum([a * b for a, b in zip(a, b)]))