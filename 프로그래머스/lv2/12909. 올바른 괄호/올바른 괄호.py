def solution(s):
    answer = 0
    for i in range(len(s)):
        if s[i] == '(':
            answer += 1
        else:
            answer -= 1
        if answer < 0 :
            return False
    if s[-1] == '(' or answer != 0:
        return False
    return True