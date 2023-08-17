def solution(citations):
    n = len(citations)
    h_index = 0

    for h in range(n+1):
        cnt = 0
        for step in citations:
            if h <= step:
                cnt += 1

        if cnt != 0 and h <= cnt:
            h_index = h

    return h_index