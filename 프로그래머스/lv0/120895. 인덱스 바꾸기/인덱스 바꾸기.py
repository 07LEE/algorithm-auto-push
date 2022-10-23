def solution(my_string, num1, num2):
    my_list = list(my_string)
    result_1 = my_string[num1]
    result_2 = my_string[num2]
    my_list[num1] = result_2
    my_list[num2] = result_1
    answer = ''
    for i in my_list:
        answer+=i
    return answer