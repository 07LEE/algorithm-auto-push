def solution(before, after):
    a = sorted(list(before))
    b = sorted(list(after))
    return 1 if a == b else 0