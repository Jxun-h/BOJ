from sys import stdin

def fibo_tf(length, fibo):
    for i in range(1, l[0] - 1):
        if fibo[i - 1] + fibo[i] != fibo[i + 1]:
            return False
    return True

for _ in range(int(stdin.readline())):
    l = list(map(int, stdin.readline().split()))
    print('YES' if fibo_tf(l[0], l[1:]) else 'NO')

