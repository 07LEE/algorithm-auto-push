M = int(input())
N = int(input())
li = []
for i in range(M, N+1):
    if i**(1/2) == int(i**(1/2)):
        li.append(i)
if sum(li) != 0:
    print(sum(li))
    print(li[0])
else:
    print(-1)