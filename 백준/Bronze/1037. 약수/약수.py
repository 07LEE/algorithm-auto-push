n = int(input())
num = sorted(list(map(int, input().split())))
print(num[0] * num[-1])