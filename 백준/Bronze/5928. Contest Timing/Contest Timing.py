d, h, m = map(int, input().split())
t = (d - 11) * 24 * 60 + h * 60 + m
print(-1) if t - 671 < 0 else print(t - 671)