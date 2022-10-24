def solution(cipher, code):
    answer = ''
    cnt = len(cipher)//code
    for i in range(1, cnt+1) :
        answer += cipher[i*code-1]
    return answer