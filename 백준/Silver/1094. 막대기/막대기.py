from sys import stdin, setrecursionlimit
import heapq
setrecursionlimit(10 ** 6)

x = int(stdin.readline())
res = 0
sticks = [64]


def solve(sticks):
    global res
    val = sum(sticks)

    if val > x:
        temp = heapq.heappop(sticks)
        heapq.heappush(sticks, temp // 2)
        heapq.heappush(sticks, temp // 2)
        
        if sum(sticks) - (temp // 2) >= x:
            heapq.heappop(sticks)
            solve(sticks)
        elif sum(sticks) >= x:
            solve(sticks)


solve(sticks)
print(len(sticks))