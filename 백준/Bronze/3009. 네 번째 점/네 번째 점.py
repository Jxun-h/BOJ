from sys import stdin
from collections import Counter
ipt = stdin.readline

xy1 =  list(map(int, ipt().split()))
xy2 =  list(map(int, ipt().split()))
xy3 =  list(map(int, ipt().split()))

x_dict = dict(Counter([xy1[0], xy2[0], xy3[0]]))
y_dict = dict(Counter([xy1[1], xy2[1], xy3[1]]))

print([k for k, v in x_dict.items() if v == 1][0], [k for k, v in y_dict.items() if v == 1][0])