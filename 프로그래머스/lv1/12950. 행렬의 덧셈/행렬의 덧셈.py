import numpy as np

def solution(arr1, arr2):
    a, b = np.array(arr1), np.array(arr2)
    answer = a+b
    return answer.tolist()