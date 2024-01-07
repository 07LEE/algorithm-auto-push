N, M = map(int, input().split())
dic = {}
for _ in range(N):
    k, v = input().split()
    dic[k] = v
for _ in range(M):
    print(dic[input()])