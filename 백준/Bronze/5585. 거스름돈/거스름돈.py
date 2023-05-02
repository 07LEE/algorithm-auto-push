n = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
resurt = 0
while n > 0 :
    for i in money:
        if n >= i:
            resurt += n//i
            n -= i*(n//i)
print(resurt)
