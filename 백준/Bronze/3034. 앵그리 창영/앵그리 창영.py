n, w, h = map(int, input().split())
for _ in range(n):
    N = int(input())
    if N <= w or N <=h or N**2 <= w**2 + h**2:
        print("DA")
    else:
        print("NE")