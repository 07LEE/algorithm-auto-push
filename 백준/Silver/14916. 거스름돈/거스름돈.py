n = int(input())

if n < 5 and n%2 != 0:
    print(-1)
elif n < 5 and n%2 == 0:
    print(n//2)
elif (n%5)%2 == 0:
    print(n//5 + (n%5)//2)
else:
    print((n//5-1) + (n%5+5)//2)