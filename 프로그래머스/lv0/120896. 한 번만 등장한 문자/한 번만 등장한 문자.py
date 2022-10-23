def solution(s):
    result = [i for i in (s) if s.count(i) == 1]
    answer = ''.join(sorted(result))
    return answer