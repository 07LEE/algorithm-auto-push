def solution(angle):
    if angle == 180 :
        answer = 4
    elif 90 < angle < 180 :
        answer = 3
    elif angle == 90:
        answer = 2 
    else:
        answer = 1

    return answer