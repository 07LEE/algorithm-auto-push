n = int(input())
ans = []
e = []

for i in range(n):
    w = input()
    if w == 'ENTER':
        ans.append(len(set(e)))
        e = []
    else :
        e.append(w)

ans.append(len(set(e)))
print(sum(ans))