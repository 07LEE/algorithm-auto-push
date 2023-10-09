x = input()
x = x.replace('XXXX', 'AAAA').replace('XX', 'BB')
print(-1) if 'X' in x else print(x)