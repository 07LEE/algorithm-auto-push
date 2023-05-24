n = int(input())
if n > 0 and (n & (n - 1)) == 0:
    print(1)
else:
    print(0)