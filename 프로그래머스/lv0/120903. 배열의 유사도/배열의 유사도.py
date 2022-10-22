def solution(s1, s2):
    result = set(s1+s2)
    answer = len(s1) + len(s2) - len(result)
    return answer