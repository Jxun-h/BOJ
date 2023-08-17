def solution(s):
    cnt = [0,0]
    word = ["p", "y"]

    for st in list(s.lower()):
        if "p" in st: cnt[0]+=1
        if "y" in st: cnt[1]+=1


    if cnt[0] != cnt[1]:
        return False

    return True