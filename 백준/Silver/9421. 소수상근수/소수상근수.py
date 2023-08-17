from sys import stdin

n = int(stdin.readline())
answer = []


def get_prime():
    p = []
    visited = [1 for _ in range(n + 1)]
    visited[0], visited[1] = 0, 0

    for i in range(2, n + 1):
        if visited[i] == 1:
            p.append(i)
            for j in range(2 * i, n + 1, i):
                visited[j] = 0

    return p


prime = get_prime()

for i in prime:
    check_dict = {}

    nums = str(i)

    while 1:
        temp = sum(map(lambda x: int(x) ** 2, nums))
        index = int(temp)
        if temp == 1:
            answer.append(i)
            break

        if check_dict.get(index):
            break

        else:
            check_dict[index] = 1

        nums = str(temp)


answer.sort()
for i in answer:
    print(i)
