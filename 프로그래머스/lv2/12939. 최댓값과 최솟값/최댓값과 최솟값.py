def solution(s):
    s_list = sorted(list(map(int, s.split())))
    answer = str(s_list[0]) +' '+ str(s_list[-1])
    return answer