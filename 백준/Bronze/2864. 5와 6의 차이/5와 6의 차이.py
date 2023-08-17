from sys import stdin

a, b = stdin.readline().split()

#min
a1 = a.replace('6', '5')
b1 = b.replace('6', '5')
print(int(a1) + int(b1), end=' ')


# max
a1 = a.replace('5', '6')
b1 = b.replace('5', '6')
print(int(a1) + int(b1))