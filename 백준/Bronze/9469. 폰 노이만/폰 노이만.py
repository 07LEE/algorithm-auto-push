P = int(input())
for _ in range(P):
    N, D, A, B, F = map(float, input().split())
    ans = D / (A + B) * F
    print(int(N), f'{ans:.6f}')