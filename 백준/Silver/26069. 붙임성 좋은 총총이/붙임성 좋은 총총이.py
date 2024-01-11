N = int(input())
cc = ['ChongChong']
for _ in range(N):
    a, b = input().split()
    if a in cc or b in cc:
        cc.append(a)
        cc.append(b)
print(len(set(cc)))