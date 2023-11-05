import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    ans = list()
    p = list(map(int, input().split()))
    for j in range(len(p)//2):
        target = p.pop(0)
        ans.append(target)
        p.remove(target//3*4)
    print(f'Case #{i+1}:', *ans)