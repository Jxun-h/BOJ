from sys import stdin


def is_prime():
    arr[0] = arr[1] = False

    for i in range(int(1e5 + 1) // 2 - 1):
        if i is True:
            temp = i
            while temp < (int(1e5 + 1) // 2):
                temp += temp
                arr[temp] = False


arr = [True for _ in range(int(1e5 + 1) // 2 - 1)]
is_prime()

for _ in range(int(stdin.readline())):
    res = {}
    n = int(stdin.readline())

    for i in range(2, int(1e5) // 2 - 1):
        if i * i > n:
            break
            
        while arr[i] and n % i == 0:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1

            n //= i

    if n != 1:
        if n not in res:
            res[n] = 1
        else:
            res[n] += 1

    for key, val in res.items():
        print(key, val)
