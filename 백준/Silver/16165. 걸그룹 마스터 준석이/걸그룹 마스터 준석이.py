n, m = map(int, input().split())
ans = []
o = {}
z = {}

for _ in range(n):
    team = input()
    num = int(input())
    name_list = []
    for _ in range(num):
        name_list.append(input())
    for name in name_list:
        o[name] = team
    z[team] = name_list

for _ in range(m):
    q = input()
    a = int(input())
    if a == 0:
        ans += sorted(z[q])
    else:
        ans.append(o[q])

for i in ans:
    print(i)