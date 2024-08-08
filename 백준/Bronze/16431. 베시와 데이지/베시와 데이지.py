br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())

b = max(abs(br-jr), abs(bc-jc))
d = abs(dr-jr) + abs(dc-jc)

if b < d:
    print('bessie')
elif b == d:
    print('tie')
else:
    print('daisy')