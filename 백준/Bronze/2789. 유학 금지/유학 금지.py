m = 'CAMBRIDGE'
n = input()
for i in m:
    if i in n:
        n = n.replace(i,'')
print(n)