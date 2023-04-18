N = int(input())
cnt = 0
for _ in range(N):
    i = int(input()[2:])
    if i <= 90 :
        cnt += 1
print(cnt)