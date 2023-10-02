n = input()
ans = set()
for i in range(len(n)):
    for j in range(len(n)):
        ans.add(n[i:j+1])
print(len(ans)-1)