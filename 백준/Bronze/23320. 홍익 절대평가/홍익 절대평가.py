n = int(input())
a = list(map(int, input().split()))
x, y = map(int, input().split())
print((n * x)//100, sum(1 for i in a if i >= y))