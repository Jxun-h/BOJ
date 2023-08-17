from sys import stdin

ipt = stdin.readline()

pay = int(ipt.rstrip())

changes = 1000 - pay

coin_list = [500, 100, 50, 10, 5, 1]
coin_count = 0


for coin in coin_list:
    if changes == 0:
        break
    elif coin > changes:
        continue
    else:
        coin_count += changes // coin
        changes %= coin

print(coin_count, end='')