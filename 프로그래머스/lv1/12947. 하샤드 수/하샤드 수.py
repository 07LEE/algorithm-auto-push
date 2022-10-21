def solution(x):
    if x < 10:
        return True
    y = sum([int(i) for i in str(x)])
    return True if x%y == 0 else False
    