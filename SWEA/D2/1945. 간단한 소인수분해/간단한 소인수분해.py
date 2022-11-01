T = int(input())
N = [2, 3, 5, 7, 11]
for t in range(1, T+1):
    n = int(input())
    N_cnt = []
    for i in N:
        cnt = 0
        while True:
            if n%i == 0:
                cnt += 1; n = n/i
            else:
                N_cnt.append(str(cnt))
                break
    print('#%s %s'%(t,' '.join(N_cnt)))