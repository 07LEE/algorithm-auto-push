N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    CNT = sum([tree - mid for tree in trees if tree > mid])
    if CNT >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)