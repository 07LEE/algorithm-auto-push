ans = 0
for i in range(1, 4):
    ans += int(input()) * i
print('happy') if ans >= 10 else print('sad')