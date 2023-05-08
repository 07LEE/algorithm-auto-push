def solution(num_list):
    if len(num_list) > 10:
        answer = sum(num_list)
    else:
        answer = 1
        for i in num_list:
            answer *= i
    return answer