ans = []
for i in range(1, 6):
    n = input()
    if 'FBI' in n:
        ans.append(i)

if len(ans) == 0:
    print('HE GOT AWAY!')
else:
    print(*ans)