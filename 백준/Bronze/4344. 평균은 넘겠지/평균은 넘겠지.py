def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

for _ in range(int(input())):
    c = list(map(int, input().split()))
    avg = sum(c[1:])/c[0]
    cnt = 0
    for i in c[1:]:
        if i > avg:
            cnt += 1
    rate = roundTraditional(cnt/c[0] *100, 3)
    
    print(f'{rate:.3f}%')