T = int(input())

for i in range(T):
    x = input()
    while '()' in x :
        x = x.replace('()', '')
    print('YES') if len(x) == 0 else print('NO')