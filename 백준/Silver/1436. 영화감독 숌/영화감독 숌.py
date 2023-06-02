n = int(input())
ans = 666

while n != 0:
    if '666' in str(ans):
        n -= 1
    if n == 0:
        break
    ans += 1
    
print(ans)