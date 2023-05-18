t = int(input())
for _ in range(t):
    s = int(input())
    n = int(input())
    qp = []
    if n == 0:
        print(s)
    else:
        for _ in range(n):
            q, p = map(int, input().split())
            qp.append(p*q)
        print(s + sum(qp))