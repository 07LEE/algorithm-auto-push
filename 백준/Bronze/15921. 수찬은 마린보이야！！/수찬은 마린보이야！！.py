N = int(input())
if N == 0 :
    print('divide by zero')
else :
    S = list(map(int, input().split()))
    S_expect = sum((i * (S.count(i)/N)) for i in set(S))
    S_avr = sum(S)/N
    print('%.2f' %(S_avr/S_expect))