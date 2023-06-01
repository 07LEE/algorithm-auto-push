t = 1
while True :
    l, p, v = map(int, input().split())
    if l == p == v == 0 :
        break
    ans = l * (v//p) + min(v%p, l)
    print(f'Case {t}: {ans}')
    t += 1