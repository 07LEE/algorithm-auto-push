num = [n for n in [int(input()) for _ in range(7)] if n % 2 != 0]
if len(num) == 0 :
    print(-1)
else :
    print(sum(num))
    print(min(num))