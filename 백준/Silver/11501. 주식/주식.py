from sys import stdin

for tc in range(int(stdin.readline())):
    n = int(stdin.readline())
    days = list(map(int, stdin.readline().split()))
    m_val, money = 0, 0

    for i in range(n - 1, -1, -1):
        if m_val < days[i]:
            m_val = days[i]
        elif m_val > days[i]:
            money += (m_val - days[i])

    print(money)