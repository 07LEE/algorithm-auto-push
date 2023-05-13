def solution(x):
    answer = True
    if x % sum([int(i) for i in str(x)]) != 0:
        answer = False
    return answer