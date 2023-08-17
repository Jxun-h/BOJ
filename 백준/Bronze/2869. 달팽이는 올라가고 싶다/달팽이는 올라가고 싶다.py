from sys import stdin

a, b, v = map(int, stdin.readline().split())
print((v - b) // (a - b) if (v - b) % (a - b) == 0 else (v - b) // (a - b) + 1)