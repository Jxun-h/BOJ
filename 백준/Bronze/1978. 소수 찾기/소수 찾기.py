from sys import stdin

n = int(stdin.readline())
prime = [1 for _ in range(1001)]
prime[0], prime[1] = 0, 0


def check():
    for i in range(2, 1001):
        if prime[i] == 1:
            temp = i + i
            while temp < 1001:
                prime[temp] = 0
                temp += i


ans = 0
check()
for i in list(map(int, stdin.readline().split())):
    if prime[i]:
        ans += 1

print(ans)