def solution(n):
    answer = n**(1/2)
    return 1 if answer == round(answer) else 2