n, k = map(int, input().split())
a = sorted([int(input()) for i in range(n)], reverse=True)
resurt = 0

while k > 0 :
    for i in a:
        if k >= i:
            resurt += k//i
            k -= i*(k//i)

print(resurt)