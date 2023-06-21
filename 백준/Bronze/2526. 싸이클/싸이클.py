n, p = map(int, input().split())
li = [n, (n*n)%p]
while True:
    num = li[-1] * n % p
    if num in li:
        break
    else:
        li.append(num)

i = li.index(num)
print(len(li[i:]))