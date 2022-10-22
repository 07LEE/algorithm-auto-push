def solution(my_string):
    answer = ''
    result = [i for i in my_string]
    
    for i in result :
        if i.isupper() == True:
            answer += i.lower()
        else :
            answer += i.upper()
            
    return answer