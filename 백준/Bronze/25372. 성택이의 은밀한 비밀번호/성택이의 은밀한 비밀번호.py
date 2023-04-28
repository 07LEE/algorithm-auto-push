N = int(input())
for _ in range(N):
    n = len(input())
    print('yes') if n <= 9 and n >= 6 else print('no')