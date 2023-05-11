def solution(code):
    answer = ''
    mode = 1
    for i, code in enumerate(code):
        if code == '1':
            mode *= -1
        elif mode == 1 and i%2 == 0:
            answer += code
        elif mode != 1 and i%2 != 0:
            answer += code
    return answer if answer != '' else 'EMPTY'