num = sorted(list(map(int, input().split())))
for i in input():
    print(num[ord(i)-ord('A')], end = ' ')