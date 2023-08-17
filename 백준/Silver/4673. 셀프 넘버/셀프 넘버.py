def self_number():
    li = []
    for i in range(1,10000):
        li.append(i + sum([int(j) for j in str(i)]))

    return sorted(list(set(range(1,10000)) - set(li)))


for self_num in self_number():
    print(self_num)