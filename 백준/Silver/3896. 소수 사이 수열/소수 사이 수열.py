from sys import stdin
from bisect import bisect_left


def get_prime():
    res = []

    for i in range(2, arr_length):
        temp = i
        if prime_tf[i] == 0:
            prime_tf[i] = 1
            res.append(i)

            while 1:
                temp += i
                if temp < arr_length + 1:
                    prime_tf[temp] = -1
                else:
                    break

    return res


nums = []
k = int(stdin.readline())
for _ in range(k):
    nums.append(int(stdin.readline()))

arr_length = 1400000
prime_tf = [0 for _ in range(arr_length + 1)]
prime = get_prime()

for i in range(k):
    if prime_tf[nums[i]] == 1:
        print(0)
    else:
        idx = bisect_left(prime, nums[i]) - 1
        print(prime[idx + 1] - prime[idx])