n = str(input())
check = [0] * 10

for i in range(10):
    check[i] = n.count(str(i))

check[6], check[9] = (check[6] + check[9] + 1)//2 , (check[6] + check[9] + 1)//2
print(max(check))