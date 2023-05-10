while True:
    num = sorted(list(map(int, input().split())))
    if sum(num) == 0:
        break
    if len(set(num)) == 1:
        print('Equilateral')
    elif num[0] + num[1] <= num[2]:
        print('Invalid')
    elif len(set(num)) == 2:
        print('Isosceles')
    else :
        print('Scalene')