from sys import stdin

n = int(stdin.readline())
prime_tf = [1 for _ in range(n + 1)]
prime_tf[0], prime_tf[1] = 0, 0
prime_nums = []


def prime():
    for i in range(2, n + 1):
        if prime_tf[i] == 1:
            temp = 2
            prime_nums.append(i)
            while i * temp <= n:
                prime_tf[i * temp] = 0
                temp += 1


prime()
ans, mod = 1, 987654321

for p in prime_nums:
    if p > n:
        break
    k = p
    while k * p <= n:
        k *= p
    ans = (ans * k) % mod

print(ans)
