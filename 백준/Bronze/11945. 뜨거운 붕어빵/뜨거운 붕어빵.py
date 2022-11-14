N, M = map(int, input().split())
B = [input() for _ in range(N)]
for i in B:
    print(i[::-1])