n = list(map(int, input().split()))
n2 = sum([i*i for i in n])%10
print(n2)