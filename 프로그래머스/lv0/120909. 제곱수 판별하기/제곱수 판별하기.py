def solution(n):
    answer = n**(1/2)
    if answer == round(answer):
        return 1
    else:
        return 2