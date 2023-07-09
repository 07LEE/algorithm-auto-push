def solution(sizes):
    x, y = [], []
    for i in sizes:
        x.append(min(i))
        y.append(max(i))
    answer = max(x) * max(y)
    return answer