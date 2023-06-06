import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    name = input().rstrip()
    dic[i], dic[name] = name, i

for _ in range(m):
    i = input().rstrip()
    print(dic[int(i)]) if i.isdigit() else print(dic[i])