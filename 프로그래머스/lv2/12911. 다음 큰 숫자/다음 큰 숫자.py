def solution(n):
    answer = 0
    cnt = bin(n).count("1")
    for num in range(n + 1, 1000001):
        num_cnt = bin(num).count("1")
        if cnt == num_cnt:
            answer = num
            break
    return answer