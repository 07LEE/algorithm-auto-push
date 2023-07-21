n = [int(i) for i in list(input())]
cnt = 0

while len(n) != 1:
    n = list(str(sum(n)))
    cnt += 1
    n = [int(i) for i in n]
    
print(cnt)
print('YES') if n[0]%3 == 0 else print('NO')