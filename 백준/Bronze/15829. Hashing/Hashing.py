l = int(input())
n = input()
ans = 0
for i in range(l):
    ans += (ord(n[i]) - 96) * (31 ** i)

print(ans)