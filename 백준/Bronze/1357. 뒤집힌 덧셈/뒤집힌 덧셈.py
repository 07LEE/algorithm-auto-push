x, y = map(str, input().split())
ans = str(int(x[::-1]) + int(y[::-1]))
print(int(ans[::-1]))