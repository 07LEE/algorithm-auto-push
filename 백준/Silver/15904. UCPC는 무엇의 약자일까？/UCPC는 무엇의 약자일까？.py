n = input()
alps = ['U', 'C', 'P', 'C']
UCPC = True

for alp in alps:
    if alp in n:
        n = n[n.index(alp)+1:]
    else:
        print('I hate UCPC')
        UCPC = False
        break

if UCPC is True:
    print('I love UCPC')