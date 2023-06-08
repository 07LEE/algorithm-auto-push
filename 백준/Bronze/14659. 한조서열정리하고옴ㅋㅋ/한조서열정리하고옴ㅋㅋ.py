n = int(input())
li = list(map(int, input().split()))

ans = []
cnt = 0
num = 0
for i in range(n):
    if li[i] > num :
        num = li[i]
        ans.append(cnt)
        cnt = 0
    else:
        cnt += 1
ans.append(cnt)
print(max(ans))