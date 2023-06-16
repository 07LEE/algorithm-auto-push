s = input()
cnt = 0
n = '?'

for i in s:
    if i != n:
        n = i
        cnt += 1

print(cnt//2)