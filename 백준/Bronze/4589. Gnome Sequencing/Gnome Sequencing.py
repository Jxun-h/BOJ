print('Gnomes:')
for _ in range(int(input())):
    data = list(map(int, input().split()))
    temp1, temp2 = sorted(data), sorted(data, reverse=True)
    if data == temp1 or data == temp2:
        print('Ordered')
    else:
        print('Unordered')