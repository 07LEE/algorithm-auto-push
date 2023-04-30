A, B, C = map(int, input().split())
D = int(input())
T = (A * 3600 + B * 60 + C + D) % (24 * 3600)
print(T // 3600, (T % 3600) // 60, T % 60)