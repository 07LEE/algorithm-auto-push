N, M, B = map(int, input().split())
block = []
min_time = 500 * 500 * 2 * 257
ans = 0

for _ in range(N):
    block += list(map(int, input().split()))

sum_block = sum(block)

for i in range(min(block), max(block)+1):
    if sum_block + B >= i * N * M:
        time = 0
        for j in block:
            if i - j <= 0:
                time -= (i - j) * 2
            else:
                time += (i - j)
        if time <= min_time:
            min_time = time
            ans = i

print(min_time, ans)