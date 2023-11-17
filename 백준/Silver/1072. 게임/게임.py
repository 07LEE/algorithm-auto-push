X, Y = map(int, input().split())
Z = (Y * 100) // X

if Z >= 99:
    print(-1)
else:
    ans = 0
    L = 1
    R = X
    while L <= R:
        mid = (L+R)//2
        if (Y+mid)*100//(X+mid) <= Z:
            L = mid + 1
        else:
            ans = mid
            R = mid - 1
    print(ans)