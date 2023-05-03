n = int(input())
s = input().split('0')
result = 0

for i in s:
    a = i.count('1')  
    result += (a*(a+1))//2

print(result)