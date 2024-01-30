A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = [0, 0]
for i in range(10):
    if A[i] > B[i]:
        ans[0] += 1
    elif A[i] < B[i]:
        ans[1] += 1

if ans[0] == ans[1]:
    print('D')
elif ans[0] > ans[1]:
    print('A')
else:
    print('B')