from sys import stdin
import math

n = int(stdin.readline().rstrip())

if n < 4:
    print(0)

else:
    print(int(math.factorial(n-1) / (math.factorial(n-1-3) * math.factorial(3))))