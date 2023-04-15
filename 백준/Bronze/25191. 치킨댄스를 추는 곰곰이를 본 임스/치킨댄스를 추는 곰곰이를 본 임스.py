N = int(input())
A, B = map(int, input().split())
print(A//2 + B) if (A//2 + B) < N else print(N)