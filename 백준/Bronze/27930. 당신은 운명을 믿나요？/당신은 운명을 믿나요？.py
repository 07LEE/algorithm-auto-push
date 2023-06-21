s = input()
k, y = 'KOREA', 'YONSEI'

kn, yn = 0, 0

for i in s:
    if i == k[kn]:
        kn += 1
    elif i == y[yn]:
        yn += 1
    
    if kn == 5:
        print(k)
        break
    if yn == 6:
        print(y)
        break