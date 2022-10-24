def solution(emergency):
    answer = []
    answer_dic = {}
    
    em = sorted(emergency, reverse=True)
    
    for i in range(len(em)):
        answer_dic[em[i]] = i+1

    for i in emergency :
        answer.append(answer_dic[i])
        
    return answer