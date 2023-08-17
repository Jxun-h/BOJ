def solution(x, n):
    if x<0:
        return [x for x in range(x, n*x-1, x)]
    elif x>0:
        return [x for x in range(x, n*x+1, x)]
    elif x==0:
        return [0]*n