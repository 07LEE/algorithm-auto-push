n = int(input())
money = []
ans = 0
for i in range(n):
    money.append(int(input()))
money.sort(reverse=True)

for i in range(n):
    if money[i]-i > 0:
        ans += money[i]-i
print(ans)