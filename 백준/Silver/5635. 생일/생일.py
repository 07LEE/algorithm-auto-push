import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    n,d,m,y = input().split()
    d,m,y = map(int,(d,m,y))
    lst.append((y,m,d,n))
lst.sort()

print(lst[-1][3])
print(lst[0][3])