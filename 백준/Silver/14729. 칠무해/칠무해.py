N = int(input())
ans = sorted([float(input()) for i in range(7)])
for i in range(N-7):
    num = float(input())
    if num < ans[-1]:
        ans[-1] = num
        ans.sort()

for i in ans:
    print(f'{i:.3f}')