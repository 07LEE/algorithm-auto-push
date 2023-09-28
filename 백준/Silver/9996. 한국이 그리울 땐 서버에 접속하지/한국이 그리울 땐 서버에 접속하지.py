import re
n = int(input())
pattern = re.compile(input().replace('*', '.*'))

for _ in range(n):
    m = input()
    if pattern.fullmatch(m):
        print('DA')
    else:
        print('NE')