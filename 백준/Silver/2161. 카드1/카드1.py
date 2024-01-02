n = [i for i in range(1, int(input()) + 1)]
ans = []
while len(n) != 0:
    ans.append(n.pop(0))
    if len(n) != 0:
        n.append(n.pop(0))
print(*ans)