def solution(num_list):
    a, b = 1, sum(num_list)**2
    for i in num_list:
        a *= i    
    if a<b:
        return 1
    else:
        return 0