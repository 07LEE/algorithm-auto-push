n = int(input())
m = input()

s = m.count('S')
l = m.count('LL')

print(n) if n < s+l+1 else print(s+l+1) 