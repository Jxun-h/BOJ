from sys import stdin

n, c = map(int, stdin.readline().split())
prices = list(map(int, stdin.readline().split()))
tf = False
arr = [0 for _ in range(10 ** 8 + 1)]

for k in range(n):
    arr[prices[k]] = 1

if arr[c]:
    tf = True
    
else:
    for k in range(n):
        for j in range(k + 1, n):
            if prices[k] + prices[j] == c:
                tf = True
                break

            elif prices[k] + prices[j] < c:
                temp = c - (prices[k] + prices[j])
                if arr[temp] and temp != prices[k] and temp != prices[j]:
                    tf = True
                    break

        if tf:
            break

print(1 if tf else 0)