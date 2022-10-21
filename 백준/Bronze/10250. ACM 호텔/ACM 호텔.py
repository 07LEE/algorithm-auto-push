T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    a = (N-1)%H+1
    b = (N-1)//H+1
    print(a*100+b)