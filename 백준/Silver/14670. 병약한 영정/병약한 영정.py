n = int(input())
dic = {}
for _ in range(n):
    e, n = map(int, input().split())
    dic[e] = n

r = int(input())
for _ in range(r):
    s = list(map(int, input().split()))[1:]
    ans = ''
    try:
        for i in s:
            ans += str(dic[i]) + ' '
        print(ans)
    except:
        print('YOU DIED')