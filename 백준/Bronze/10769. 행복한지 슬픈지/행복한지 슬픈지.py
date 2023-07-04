n = input()
h = n.count(':-)')
s = n.count(':-(')
print('none') if h == 0 and s == 0 else print('happy') if h > s else print('sad') if s > h else print('unsure')