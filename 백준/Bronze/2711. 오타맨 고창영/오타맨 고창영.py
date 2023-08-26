n = int(input())
for _ in range(n):
    ans = ''
    a, b = input().split()
    b = list(b)
    b.pop(int(a)-1)
    for i in b:
        ans += i
    print(ans)