t = int(input())
for i in range(1, t+1):
    w = list(map(str, input().split()))
    W = ' '.join(w[::-1])
    print(f'Case #{i}: {W}')