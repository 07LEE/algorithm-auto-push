t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))