n = int(input())
ans = [list(input().split()) for _ in range(n)]
ans.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in ans:
    print(i[0])