k, n = map(int, input().split())

lan_cables = []
for _ in range(k):
    lan_cables.append(int(input()))

start, end = 1, max(lan_cables)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for lan in lan_cables:
        cnt += lan // mid

    if cnt >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)