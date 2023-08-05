n = int(input())
s = [int(input()) for _ in range(n)]

cnt = 0 

for i in range(n-2, -1, -1):
    if s[i] >= s[i+1]:
        cnt += s[i] - s[i+1] + 1
        s[i] = s[i+1] - 1

print(cnt)