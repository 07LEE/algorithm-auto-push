def solution(order):
    answer = 0
    answer += str(order).count('3')
    answer += str(order).count('6')
    answer += str(order).count('9')
    return answer