def solution(num_list):
    eve = ''
    odd = ''
    for i in num_list:
        if i % 2 == 0 :
            eve += str(i)
        else :
            odd += str(i)
    answer = int(eve) + int(odd)
    return answer