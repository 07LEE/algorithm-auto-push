m = input().split('-')
p = [sum(map(int, i.split('+'))) for i in m]
ans = p[0]
for i in p[1:]:
    ans -= i
print(ans)