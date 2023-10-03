n = int(input())
ans = [0] * (n+1)

if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        j = list(str(i))
        if int(j[1]) * 2 == int(j[0]) + int(j[2]):
            ans[i] = 1
    print(sum(ans)+99)