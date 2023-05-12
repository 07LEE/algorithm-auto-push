def solution(n):
    if n == 1 :
        answer = '수'
    else :
        answer = '수박'
        answer *= n//2
        if n % 2 != 0:
            answer += '수'            
    return answer