def solution(balls, share):
    a = balls - share
    n = 1
    nm = 1 
    m = 1
    for i in range(1, balls+1) :
        n = n * i
    for i in range(1, a+1) :
        nm = nm * i
    for i in range(1, share+1) :
        m = m * i
    answer = n/(nm*m)
    return answer