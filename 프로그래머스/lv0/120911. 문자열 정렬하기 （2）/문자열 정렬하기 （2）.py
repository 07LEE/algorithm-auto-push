def solution(my_string):
    string = [i for i in my_string.lower()]
    answer = ''.join(sorted(string))
    return answer