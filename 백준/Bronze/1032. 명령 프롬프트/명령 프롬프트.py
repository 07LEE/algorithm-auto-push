N = int(input())
W = list(input())
if N == 1:
    print(''.join(W))
else :
    for _ in range(N-1):
        w = input()
        for i in range(len(W)):
            if W[i] != w[i]:
                W[i] = '?'                 
    print(''.join(W))