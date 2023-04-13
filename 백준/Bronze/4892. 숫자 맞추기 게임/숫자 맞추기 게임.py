n = 0
while True:

    n0 = int(input())

    if n0 == 0 :
        break
    else :
        n += 1

    n1 = 3 * n0

    if n1 % 2 == 0 :
        n2 = n1/2
        a = 'even'
    else :
        n2 = (n1+1) /2
        a = 'odd'

    n3 = n2*3
    n4 = int(n3/9)

    print(f'{n}. {a} {n4}')