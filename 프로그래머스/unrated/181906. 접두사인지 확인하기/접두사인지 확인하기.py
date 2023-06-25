def solution(my_string, is_prefix):
    if is_prefix in my_string:
        for i in range(len(is_prefix)):
            if my_string[i] != is_prefix[i]:
                return 0
        return 1
    else:
        return 0