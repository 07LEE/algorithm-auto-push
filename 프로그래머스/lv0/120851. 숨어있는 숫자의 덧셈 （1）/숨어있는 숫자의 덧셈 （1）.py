def solution(my_string):
    import re
    n = str(re.sub(r'[^0-9]', '', my_string))
    answer = sum([int(i) for i in str(n)])
    return answer