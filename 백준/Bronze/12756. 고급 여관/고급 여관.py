from math import ceil

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

a = ceil(a2/b1)
b = ceil(b2/a1)

print("PLAYER A" if a > b else "PLAYER B" if b > a else "DRAW")