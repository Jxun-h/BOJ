import math as m

def solution(n):
    p = m.sqrt(n)
    if p.is_integer():
        return pow(p+1, 2)
    else:
        return -1