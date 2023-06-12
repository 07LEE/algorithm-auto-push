n = int(input())

a = [0]*1001
a[1]=1
a[2]=2

for i in range(3,1001):
  a[i] = (a[i-1]+a[i-2])%10007

print(a[n])