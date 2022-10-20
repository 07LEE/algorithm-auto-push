n = int(input())
for i in range(n):
    a = sum(map(int, str(i)))
    b = i + a
    if b == n :
        print(i)
        break
else :
    print(0)