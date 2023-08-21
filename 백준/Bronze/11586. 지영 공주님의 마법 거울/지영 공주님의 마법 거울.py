n = int(input())
m = [input() for _ in range(n)]
k = int(input())

if k == 1:
    for i in m:
        print(i)
elif k == 2:
    for i in m:
        print(i[::-1])
elif k ==3:
    for i in range(1, n+1):
        print(m[-i])