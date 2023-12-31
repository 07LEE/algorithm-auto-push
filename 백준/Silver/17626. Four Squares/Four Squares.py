n = int(input())
ans = [0, 1]
for i in range(2, n+1):
    min_num = 4
    for j in range(1, int(i ** 0.5) + 1):
        min_num = min(min_num, ans[i - (j ** 2)])
    ans.append(min_num + 1)
print(ans[n])