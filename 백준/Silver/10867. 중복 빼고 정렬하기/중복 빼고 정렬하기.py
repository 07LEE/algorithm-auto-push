n = int(input())
m = sorted(list(set(map(int, input().split(' ')))))
print(*m)