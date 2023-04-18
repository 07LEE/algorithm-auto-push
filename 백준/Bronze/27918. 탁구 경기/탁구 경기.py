N = int(input())
D = P = 0
for _ in range(N):
    if input() == 'D':
        D += 1
    else :
        P += 1

    if abs(D-P) == 2:
        break
print(f'{D}:{P}')
