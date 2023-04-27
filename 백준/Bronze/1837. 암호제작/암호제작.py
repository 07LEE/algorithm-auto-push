P, K = map(int, input().split())
true = True
for i in range(2, K):
    if P%i == 0 :
        print(f'BAD {i}')
        true = False
        break

if true:
    print('GOOD')