dp = [0, 1, 2, 3, 5]
N = int(input())
if N <= 4:
    print(dp[N]%15746)
else:
    for i in range(4, N+1):
        dp.append((dp[i] + dp[i-1])%15746)
    print(dp[N])