import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a, b= [], []

for _ in range(n):
    a.append(input().rstrip())

for _ in range(m):
    b.append(input().rstrip())

ans = sorted(list(set(a).intersection(b)))

print(len(ans))
for i in ans:
    print(i)