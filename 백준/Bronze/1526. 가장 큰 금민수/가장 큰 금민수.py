n = int(input())

while True:
    m = True
    for i in str(n):
        if i != '4' and i != '7':
            m = False
            n -= 1
    if m:
        print(n)
        break