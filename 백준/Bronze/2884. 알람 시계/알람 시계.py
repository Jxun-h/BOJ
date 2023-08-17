import datetime
from sys import stdin

a, b = stdin.readline().rstrip().split()
k = datetime.datetime.strptime('{}:{}'.format(a, b), "%H:%M")
print(*list(map(int, datetime.datetime.strftime(k - datetime.timedelta(minutes=45), "%H:%M").split(':'))))