x, y = map(int, input().split())
if y < 45 :
    y += 15
    x -= 1
    if x<0:
        x = 23
else:
    y -= 45
print(x, y)