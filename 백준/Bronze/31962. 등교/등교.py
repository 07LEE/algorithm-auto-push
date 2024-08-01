N, X = map(int, input().split())
ans = -1
for _ in range(N):
    S, T = map(int, input().split())
    if S + T <= X and S > ans:
        ans = S
print(ans)