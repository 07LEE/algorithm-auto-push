import math
N = str(math.factorial(int(input())))[::-1]
for i in range(len(N)):
    if N[i] != '0':
        print(i)
        break