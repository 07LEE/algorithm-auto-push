def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
ans = list(map(int, input().split()))
for i in range(len(ans)-1):
    m = gcd(ans[0], ans[i+1])
    print(f'{int(ans[0]/m)}/{int(ans[i+1]/m)}')