def solution(n):
    answer = 1
    i = 6
    while True:
        if (answer*i)%n == 0:
            return answer
        else:
            answer += 1