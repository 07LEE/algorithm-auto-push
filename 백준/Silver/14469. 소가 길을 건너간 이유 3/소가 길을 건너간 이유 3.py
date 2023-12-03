n = int(input())
caw = sorted([list(map(int, input().split())) for _ in range(n)])
time = 0
for i, j in caw:
    if time < i:
        time = i
    time += j
print(time)