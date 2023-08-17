def solution(ineq, eq, n, m):
    
    temp = ineq + eq
    if temp == ">=":
        answer = 1 if n >= m else 0
    elif temp == "<=":
        answer = 1 if n <= m else 0
    elif temp == ">!":
        answer = 1 if n > m else 0
    else:
        answer = 1 if n < m else 0
    
    
    return answer