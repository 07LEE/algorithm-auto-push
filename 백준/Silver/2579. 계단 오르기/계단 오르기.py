n = int(input())
m = [int(input()) for _ in range(n)]
dp = [0] * n

if len(m) <= 2:
    print(sum(m))

else:
    dp[0] = m[0]
    dp[1] = m[0] + m[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + m[i-1] + m[i], dp[i-2] + m[i])
    print(dp[-1])