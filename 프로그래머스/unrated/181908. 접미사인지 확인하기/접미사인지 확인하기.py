def solution(my_string, is_suffix):
    end = my_string[len(my_string) - len(is_suffix):]
    if end == is_suffix:
        answer = 1
    else:
        answer = 0
    return answer