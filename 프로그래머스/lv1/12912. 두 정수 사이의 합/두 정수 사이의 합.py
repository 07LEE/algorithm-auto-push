def solution(a, b):
    n = [a, b]
    n = sorted(n)
    answer = 0
    
    for i in range(n[0], n[1]+1):
        answer += i
        
    if a == b :
        return a
        
    return answer