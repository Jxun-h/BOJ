data = list(map(int, input().split()))
print(1 if data.count(1) > data.count(2) else 2)