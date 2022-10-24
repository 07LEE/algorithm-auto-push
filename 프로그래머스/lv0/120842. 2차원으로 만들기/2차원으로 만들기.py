def solution(num_list, n):
    answer = []
    a = []
    for i in num_list :
        a.append(i)
        if len(a) == n:
            answer.append(a)
            a = []

    return answer