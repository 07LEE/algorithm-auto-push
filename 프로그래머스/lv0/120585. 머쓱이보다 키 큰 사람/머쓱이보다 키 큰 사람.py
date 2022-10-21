def solution(array, height):
    answer = len([i for i in array if i > height])
    return answer