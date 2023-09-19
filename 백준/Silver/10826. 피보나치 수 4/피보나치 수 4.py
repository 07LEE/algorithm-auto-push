m = int(input())
if m < 3 :
    print(0) if m == 0 else print(1)
else:
    n = [0] * (m + 1)
    n[1], n[2] = 1, 1
    for i in range(3, m+1):
        n[i] = n[i-1] + n[i-2]
    print(n[m])