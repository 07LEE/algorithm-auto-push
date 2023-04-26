T = int(input())
for _ in range(T):
    N, st, ma, te = map(int, input().split())
    score = st + ma + te
    if score < 55 :
        answer = 'FAIL'
        print(f'{N} {score} {answer}')
    elif st < 10.5 or ma < 7.5 or te < 12 :
        answer = 'FAIL'
        print(f'{N} {score} {answer}')
    else:
        answer = 'PASS'
        print(f'{N} {score} {answer}')