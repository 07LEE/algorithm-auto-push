n = int(input())
txt1 = '* ' * ((n+1)//2)
txt2 = ' *' * ((n+1)//2)
for i in range(1, n+1):
    print(txt1[:n])
    print(txt2[:n])