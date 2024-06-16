import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
odd = -1
even = -1

for i in range(n-1):
    for j in range(i+1, n):
        k = abs(m[j] - m[i])
        if k%2 == 0:
            if even == -1:
                even = k
            else:
                if k < even:
                    even = k
                    
        else:
            if odd == -1:
                odd = k
            else:
                if k < odd:
                    odd = k

print(f'{even} {odd}')