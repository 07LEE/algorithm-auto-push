name = []
game = {'Y':1, 'F':2, 'O':3}
n, g = input().split()
for _ in range(int(n)):
    name.append(input())

print(len(list(set(name)))//game[g])