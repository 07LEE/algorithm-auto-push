x, y, z= map(int, input().split())
if x==y==z:
    print(10000+x*1000)
elif x==y or y==z:
    print(1000+y*100)
elif x==z or y==z:
    print(1000+z*100)
else:
    print(max(x,y,z)*100)