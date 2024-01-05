a = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

T = int(input())
for _ in range(T):
    s = set(input())
    b = a - s
    num = 0
    for i in b:
        num += ord(i)
    print(num)