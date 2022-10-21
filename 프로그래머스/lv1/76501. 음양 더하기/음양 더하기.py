def solution(absolutes, signs):
    answer = sum(absolutes[i] if signs[i] == True else (absolutes[i] * -1) for i in range(len(absolutes)))
    return answer