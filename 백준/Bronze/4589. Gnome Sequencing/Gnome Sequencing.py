n = int(input())
print('Gnomes:')
for _ in range(n):
    goblins = list(map(int, input().split()))
    if goblins == sorted(goblins) or goblins == sorted(goblins, reverse=True):
        print('Ordered')
    else :
        print('Unordered')