import itertools as itt
import collections

def solution(clothes):
    t_cl = [clothes[x][1] for x in range(len(clothes))]
    numofcl = list(collections.Counter(t_cl).values())
    no_cl = len(list(itt.combinations(t_cl, 0)))

    if len(numofcl) == 1:
        return numofcl[0]
    else:
        result = 1
        for step in numofcl:
            result *= step + 1

        return result - no_cl