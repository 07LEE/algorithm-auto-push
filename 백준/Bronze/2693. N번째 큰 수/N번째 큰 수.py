t = int(input())
for _ in range(t):
    n = sorted(list(map(int, input().split())))
    print(n[-3])