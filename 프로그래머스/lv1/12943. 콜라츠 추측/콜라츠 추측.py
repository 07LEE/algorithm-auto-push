def solution(num):
    answer = 0
    for _ in range(500):
        if num == 1:
            break
        elif num % 2 == 0:
            num = num//2
            answer += 1
        else:
            num = (3 * num) + 1
            answer += 1
    if answer == 500:
        answer = -1
    return answer