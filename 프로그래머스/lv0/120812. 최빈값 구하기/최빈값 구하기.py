def solution(array):
    cnt = max([array.count(i) for i in set(array)])
    answer = [i for i in set(array) if array.count(i) == cnt]
    return -1 if len(answer) != 1 else answer[0]