from sys import stdin

a, b, c = map(int, stdin.readline().split())
menu_stack = []
menu_data = {}

for _ in range(a):
    menu_name = stdin.readline().rstrip().split()
    if menu_name[0] not in menu_data:
        menu_data[menu_name[0]] = (int(menu_name[1]), 'n')

for _ in range(b):
    menu_name = stdin.readline().rstrip().split()
    if menu_name[0] not in menu_data:
        menu_data[menu_name[0]] = (int(menu_name[1]), 'sp')

for _ in range(c):
    menu_name = stdin.readline().rstrip()
    if menu_name not in menu_data:
        menu_data[menu_name] = (0, 'se')

n = int(stdin.readline())
price = [0, 0]

for _ in range(n):
    order_name = stdin.readline().rstrip()
    if menu_data[order_name][1] == 'n':
        price[0] += menu_data[order_name][0]

    elif menu_data[order_name][1] == 'sp':
        if price[0] >= 20000:
            price[1] += menu_data[order_name][0]
        else:
            menu_stack.append(order_name)

    elif menu_data[order_name][1] == 'se':
        menu_stack.append(order_name)

tf, service = True, False
while menu_stack:
    order_name = menu_stack.pop()

    if menu_data[order_name][1] == 'sp':
        if price[0] >= 20000:
            price[1] += menu_data[order_name][0]
        else:
            tf = False
            break

    elif menu_data[order_name][1] == 'se':
        if sum(price) >= 50000 and service is False:
            service = True
            continue
        else:
            tf = False
            break

print('Okay' if tf else 'No')


