t = int(input())

for _ in range(t):
    value, unit = input().split()
    value = float(value)
    
    if unit == 'kg':
        value *= 2.2046
        unit = 'lb'
    elif unit == 'lb':
        value *= 0.4536
        unit = 'kg'
    elif unit == 'l':
        value *= 0.2642
        unit = 'g'
    else: # unit == 'g'
        value *= 3.7854
        unit = 'l'
    
    print('%.4f %s' % (round(value, 4), unit))