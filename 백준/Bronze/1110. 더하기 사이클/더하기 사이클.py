n = int(input())
cnt = 0
num = n
while True:
    a = num//10
    b = num%10
    c = (a+b)%10
    num = (b*10)+c
    cnt += 1
    if num==n:
        break
print(cnt)