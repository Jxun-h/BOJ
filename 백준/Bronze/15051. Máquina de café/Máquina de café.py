from sys import stdin

A1 = int(stdin.readline())
A2 = int(stdin.readline())
A3 = int(stdin.readline())
print(min(A2*2 + A3*4, A1*2 + A3*2, A1*4 + A2*2))