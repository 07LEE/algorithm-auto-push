N = int(input())
F = [0, 1, 1]
for i in range(2, N):
    F.append(F[i-1] + F[i])
print(F[-1])