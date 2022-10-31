def solution(sizes):
    w = []
    h = []
    for i in sizes:
        j = sorted(i)
        w.append(j[0])
        h.append(j[1])
    answer = max(w) * max(h)
    return answer