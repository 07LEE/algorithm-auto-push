import math
a,b,c = list(map(int, input().split()))
print(-1 if b>c or b==c else math.floor(a/(c-b))+1)