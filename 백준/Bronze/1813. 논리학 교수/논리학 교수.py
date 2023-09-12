n = int(input())
lst = map(int, input().split())

cnt = [0] * 51
for n in lst:
    cnt[n] += 1

for i in range(50, -1, -1):
    if cnt[i] == i:
        print(i)
        break
else: 
    print(-1)