c, k, p = map(int, input().split())
ans = 0
for i in range(1, c+1):
    ans += k*i + p*i*i

print(ans)