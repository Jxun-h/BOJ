from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()
arr.sort(key=lambda x: x % 10)
answer = 0

for cake in arr:
    if m > 0:
        if cake < 10:
            continue

        elif cake % 10 == 0:
            temp = cake // 10 - 1

            if temp == 0:
                answer += 1
            else:
                if m >= temp:
                    answer += temp + 1
                    m -= temp
                else:
                    answer += m
                    break
        else:
            temp = cake // 10
            if m >= temp:
                answer += temp
                m -= temp
            else:
                answer += m
                break

    else:
        break

print(answer)