li, n = map(int, input().split())
digit = 0
for i in range(1, li+1):
    digit += str(i).count(str(n))
print(digit)