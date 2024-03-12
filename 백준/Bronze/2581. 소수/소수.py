import sys

is_prime_arr = [1 for x in range(1, 10001)]
prime = []


def is_prime():
    for i in range(2, 10000):
        if is_prime_arr[i]:
            prime.append(i)
            start = i + i
            for x in range(start, 10000, i):
                is_prime_arr[x] = False


is_prime()
answer = []
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

for i in prime:
    if n <= i <= m:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))