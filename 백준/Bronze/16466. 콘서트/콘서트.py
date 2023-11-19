import sys
input = sys.stdin.readline
N = int(input())
sold = sorted(list(map(int, input().split())))
for i in range(1,N+1) :
    if(sold[i-1] != i) :
        print(i)
        sys.exit()
print(N+1)