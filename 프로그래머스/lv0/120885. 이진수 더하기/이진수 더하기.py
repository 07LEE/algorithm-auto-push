def solution(bin1, bin2):
    a = int(bin1,2)
    b = int(bin2,2)
    answer = bin(a+b)[2:]
    return answer