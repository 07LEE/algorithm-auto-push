import math
N, A, B, C, D = map(int, input().split())
cost = [math.ceil(N/A) * B, math.ceil(N/C) * D]
print(min(cost))