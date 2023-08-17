from sys import stdin

prime = [True for _ in range(10 ** 6 + 3002)]
n = int(stdin.readline())
prime[1] = False


def is_prime(n):
    for i in range(2, n):

        if prime[i]:
            idx = 2
            while i * idx < 10 ** 6 + 3002:
                prime[i * idx] = False
                idx += 1


is_prime(n)
for i in range(n, 10 ** 6 + 3002):
    if prime[i] is True:
        temp = list(str(i))
        temp.reverse()
        if temp == list(str(i)):
            print(i)
            break
