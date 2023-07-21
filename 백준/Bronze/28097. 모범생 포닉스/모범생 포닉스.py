n = 8 * (int(input())-1)
t = sum(map(int, input().split()))
print(f'0 {n+t}') if n+t < 24 else print(f'{(n+t)//24} {(n+t)%24}')