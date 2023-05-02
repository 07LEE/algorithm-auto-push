n = int(input())
rope = sorted([int(input()) for _ in range(n)])
rope = [rope[i]*(n-i) for i in range(len(rope))]
print(max(rope))