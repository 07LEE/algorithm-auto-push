n = int(input())
num = [0, 1, 1, 1]
if n <= 3:
    print(num[n])
else:
    for i in range(3, n):
        num.append(num[i] + num[i-2])
    print(num[-1])