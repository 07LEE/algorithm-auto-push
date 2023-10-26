import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    c = dict()
    N = int(input())

    for _ in range(N):
        a, b = input().split()
        if b in c:
            c[b].append(a)
        else:
            c[b] = list()
            c[b].append(a)

    ans = 1
    for k, v in c.items():
        ans *= len(v) + 1
    print(ans - 1)