import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m = sorted(m)
odd = []
even = []


for i in range(n-1):
    for j in range(i+1, n):
        k = m[j] - m[i]
        if k%2 == 0:
            even.append(k)
        else:
            odd.append(k)

if len(odd) == 0:
    odd_ans = -1
else:
    odd_ans = min(odd)

if len(even) == 0:
    even_ans = -1
else:
    even_ans = min(even)

print(f'{even_ans} {odd_ans}')