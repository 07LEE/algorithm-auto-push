S = input()
K = input()

ans = ''
for i in S:
    try:
        int(i)
        pass
    except:        
        if i is not int():
            ans += i

print(1) if K in ans else print(0)