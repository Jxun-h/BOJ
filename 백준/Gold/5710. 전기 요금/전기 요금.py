from sys import stdin

cost = [100, 10000, 1000000]
watt_cost = [100 * 2, 100 * 2 + 9900 * 3, 100 * 2 + 9900 * 3 + 990000 * 5]


def wh_cost(wh):
    if wh <= watt_cost[0]:
        return wh // 2

    if wh <= watt_cost[1]:
        return 100 + (wh - watt_cost[0]) // 3

    if wh <= watt_cost[2]:
        return 10000 + (wh - watt_cost[1]) // 5

    return 1000000 + (wh - watt_cost[2]) // 7


def cost_wh(a):
    if cost[0] > a:
        return a * 2

    if cost[1] > a:
        return 200 + (a - cost[0]) * 3

    if cost[2] > a:
        return 200 + 9900 * 3 + (a - cost[1]) * 5

    return 200 + 9900 * 3 + 990000 * 5 + (a - cost[2]) * 7


while 1:
    a, b = map(int, stdin.readline().split())
    if a == b == 0:
        break

    wh = wh_cost(a)

    l, r = 0, wh

    while l <= r:
        mid_wh = (l + r) // 2
        other_wh = wh - mid_wh

        diff = cost_wh(mid_wh) - cost_wh(other_wh)

        if diff < b:
            l = mid_wh + 1

        elif diff > b:
            r = mid_wh - 1

        else:
            print(cost_wh(min(mid_wh, other_wh)))
            break