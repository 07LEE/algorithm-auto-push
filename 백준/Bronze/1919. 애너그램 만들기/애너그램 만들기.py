li = [0] * 26

a = list(input())
b = list(input())

for i in a :
    li[ord(i) - 97] += 1
for j in b:
    li[ord(j) - 97] -= 1

print(sum(map(abs, li)))