def solution(arr, divisor):
    answer = sorted([i for i in arr if i%divisor == 0])
    if len(answer) != 0 :
        return answer 
    else :
        answer.append(-1)
        return answer