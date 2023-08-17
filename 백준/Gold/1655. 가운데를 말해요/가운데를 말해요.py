from sys import stdin
import heapq

q = [[], []]
answer = []
for i in range(int(stdin.readline())):
    data = int(stdin.readline())
    if len(q[0]) == len(q[1]):
        heapq.heappush(q[0], (-data, data))

    else:
        heapq.heappush(q[1], (data, data))

    if q[1] and q[0][0][1] > q[1][0][0]:
        min_value = heapq.heappop(q[1])[0]
        max_value = heapq.heappop(q[0])[1]
        heapq.heappush(q[0], (-min_value, min_value))
        heapq.heappush(q[1], (max_value, max_value))

    answer.append(q[0][0][1])

for j in answer:
    print(j)