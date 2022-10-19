x, y = map(int, input().split())
t = int(input())
print((x+((t+y)//60))%24,(y+t)%60)