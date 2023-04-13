N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
print(sum([A[i] * B[i] for i in range(N)]))