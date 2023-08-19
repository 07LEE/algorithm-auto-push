n = int(input())

while True:
    m = int(input())
    if m == 0:
        break
    elif m%n == 0:
        print(f'{m} is a multiple of {n}.')
    else:
        print(f'{m} is NOT a multiple of {n}.')