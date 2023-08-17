from sys import stdin

n = int(stdin.readline().rstrip())
print("%.{}f".format(n) % pow(2, -1 * n))