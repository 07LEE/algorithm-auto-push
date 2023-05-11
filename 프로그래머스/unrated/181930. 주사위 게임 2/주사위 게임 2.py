def solution(a, b, c):
    if a == b and a == c:
        answer = (3 * a) * (3 * (a**2)) * (3*(a**3))
    elif a != b and b != c and a != c:
        answer = a + b + c
    else :
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    return answer