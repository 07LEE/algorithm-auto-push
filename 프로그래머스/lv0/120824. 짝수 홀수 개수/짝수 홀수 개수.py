def solution(num_list):
    a = len([i for i in num_list if i%2 == 0])
    b = len(num_list) - a
    answer = [a, b]
    return answer