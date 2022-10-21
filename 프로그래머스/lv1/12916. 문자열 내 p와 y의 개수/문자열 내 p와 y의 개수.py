def solution(s):
    s = s.lower()
    n = 0
    n = n + s.count('p') - s.count('y')
    return True if n == 0 else False