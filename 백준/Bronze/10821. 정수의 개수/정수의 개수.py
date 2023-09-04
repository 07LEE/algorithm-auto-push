s = list(input().split(','))
cnt = 0

for i in s:
    if int(i):
        cnt += 1

print(cnt)