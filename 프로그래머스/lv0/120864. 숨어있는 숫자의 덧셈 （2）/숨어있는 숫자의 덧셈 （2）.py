import re

def solution(my_string):
    answer = 0
    a = re.findall(r"[0-9]+", my_string)
    for i in a:
        answer += int(i)
    return answer