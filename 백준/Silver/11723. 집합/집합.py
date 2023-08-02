import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m) :
    i = list(input().strip().split(' '))    
    if len(i) == 1:
        if i[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else :
        n  = int(i[-1])
        if i[0] == 'add':
            s.add(n)
        if i[0] == 'remove' and n in s:
            s.discard(n)
        if i[0] == 'check':
            print(1 if n in s else 0)
        if i[0] == 'toggle':
            s.discard(n) if n in s else s.add(n)