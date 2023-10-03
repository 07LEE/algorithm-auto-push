n = input()
ans = sorted([n[i:] for i in range(len(n))])
for i in ans:
    print(i)