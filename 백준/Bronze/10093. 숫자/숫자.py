a, b = map(int, input().split())
if a > b:
    a, b = b, a
li = [i for i in range(a+1, b)]

if a != b:
    print(b-a-1) 
    print(*li)
else:
    print(0)