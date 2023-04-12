N = int(input())

divisors = []
for i in range(1, N+1):
    if N % i == 0:
        divisors.append(i)

for i in divisors:
    print(i, end=' ')