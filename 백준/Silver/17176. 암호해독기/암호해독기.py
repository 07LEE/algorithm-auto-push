N = int(input())
W = list(map(int, input().split()))
M = input()
dic = []

for i in M:
    if i.isspace():
        dic.append(0)
    elif i.islower():
        dic.append(ord(i) - 70)
    elif i.upper():
        dic.append(ord(i) - 64)

print('y') if sorted(W) == sorted(dic) else print('n')