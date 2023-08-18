from sys import stdin
import datetime

answer = 0
n = int(stdin.readline())
time_table = []

for _ in range(n):
    ymd, hms, point = stdin.readline().rstrip().split()
    date_string = ymd + ' ' + hms
    time_data = datetime.datetime.strptime(date_string, "%Y/%m/%d %H:%M:%S")
    time_table.append((time_data, int(point)))


bottom, top = 0, 0
for i in range(n):
    data = time_table[n - 1][0] - time_table[i][0]
    temp = (data.days * 1440 * 60 + data.seconds) / (1440 * 60) / 365
    res = max(0.5 ** temp, 0.9 ** (n - (i + 1)))
    bottom += res
    top += res * time_table[i][1]

if n != 0:
    print(round(top / bottom))
else:
    print(0)