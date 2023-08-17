from sys import stdin
def xy_factorial(n):
    if n > 1:
        return n * xy_factorial(n - 1)
    else:
        return 1
print(xy_factorial(int(stdin.readline().rstrip())))