t = int(input())
for _ in range(t):
    dp = [1, 1, 2]
    n = int(input())
    if n >= 4:
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2] + dp[i-3])
        print(dp[-1])
    elif n == 3:
        print(4)
    else:
        print(dp[n])