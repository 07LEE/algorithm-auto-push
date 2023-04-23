W = input()
T = len(W)//10
for i in range(T):
    print(W[:10])
    W = W[10:]
print(W)