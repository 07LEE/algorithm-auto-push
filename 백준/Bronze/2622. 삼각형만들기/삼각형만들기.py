from math import ceil
n = int(input())
cnt = 0

for a in range(ceil(n/3), ceil(n/2)):
    for b in range(ceil((n-a)/2), a+1):
        cnt += 1
            
print(cnt)