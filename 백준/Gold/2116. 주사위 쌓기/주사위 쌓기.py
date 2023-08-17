from sys import stdin

n = int(stdin.readline())
dices = []
bottom_top = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}


for _ in range(n):
    data = list(map(int, stdin.readline().split()))
    dices.append(data)


ans = 0
for i in range(6):
    side_max_value = []
    dice_number = [x for x in range(1, 7)]
    dice_number.remove(dices[0][i])

    next_number = dices[0][bottom_top[i]]
    dice_number.remove(next_number)
    side_max_value.append(max(dice_number))

    for j in range(1, n):
        dice_number = [x for x in range(1, 7)]
        dice_number.remove(next_number)

        next_number = dices[j][bottom_top[dices[j].index(next_number)]]
        dice_number.remove(next_number)
        side_max_value.append(max(dice_number))

    ans = max(ans, sum(side_max_value))

print(ans)

