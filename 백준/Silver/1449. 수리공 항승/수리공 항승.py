n, l = map(int, input().split())
li = sorted(list(map(int, input().split())))
cnt = 1
a = li[0]
for i in li[1:]:
    if (i+0.5)-(a-0.5) > l:
        cnt += 1
        a = i
print(cnt)