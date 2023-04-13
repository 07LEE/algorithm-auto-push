B = input()
a = 10
for i in range(len(B)-1):
    if B[i] == B[i+1]:
        a += 5
    else:
        a += 10
print(a)