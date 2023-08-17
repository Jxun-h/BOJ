count = int(input())
arr = []
for x in range(count):
    arr.append(int(input()))

arr = list(set(arr))

arr.sort()

for x in arr:
    print(x)