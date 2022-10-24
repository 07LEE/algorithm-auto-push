def solution(dots):
    x = []
    y = []
    
    for i in dots:
        x.append(i[0])
        y.append(i[1])
        
    x = list(set(x))
    y = list(set(y))
    answer = abs((x[0]-x[1])*(y[0]-y[1]))
    
    return answer