n = int(input())
t = sorted(list(map(int, input().split())), reverse=True)
day = [t[i] + i + 2 for i in range(n)]
print(max(day))