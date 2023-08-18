from sys import stdin

n, a, b, c, d = map(int, stdin.readline().split())
t1, t2 = 0, 9
if n % a != 0:
    t1 = n // a + 1
else:
    t1 = n // a

if n % c != 0:
    t2 = n // c + 1
else:
    t2 = n // c

print(min(t1 * b, t2 * d))