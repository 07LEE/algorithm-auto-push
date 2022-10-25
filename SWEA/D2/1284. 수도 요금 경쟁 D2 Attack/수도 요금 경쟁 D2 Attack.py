T = int(input())
for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    B = Q if R>=W else Q+(W-R)*S
    print('#%s'%t, B) if A>=B else print('#%s'%t, A)